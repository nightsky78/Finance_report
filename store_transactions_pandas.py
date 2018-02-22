from db_handling import db
from filehandling import read_csv_pandas
import pandas


def processtransfile(location,sourcefile,source,user_id):

    # First we need to retrieve the data for the source file

    myDB = db.Db_handler_user(user_id)

    mysource = myDB.retrieve_source_values(source)
    sourcelength = mysource[0][2]
    sourcedelimiter = mysource[0][1]
    ger_to_us_col = mysource[0][5]
    skiprow = mysource[0][7]
    incl_column = [mysource[0][3], mysource[0][4], mysource[0][5]]
    subject_column = mysource[0][4]
    add_column = mysource[0][8]
    date_column = mysource[0][3]
    source_id = mysource[0][6]

    print('Source config read: {0}'.format(mysource))
    # Now find the columns to delete with Pandas method
    x = 0
    excl_columns = []
    while x < sourcelength:
        if x not in incl_column:
            excl_columns.append(x)
        x = x + 1

    # getting data back with the pandas file
    MyContent = read_csv_pandas.ReadCsvPandas(sourcefile,location)


    content = MyContent.get_pandas_content(skiprow,excl_columns, sourcedelimiter, add_column, subject_column)

    # Check if oldest entry in Excel file is newer than newest entry in Database for this sourcefile
    # Get newest entry from database
    newest_from_db = myDB.select_from_db('transactions', 'max(date)', 'source_id = {0}'.format(source_id))[0][0]

    # get oldest entry from sourcefile.sourcetype
    oldest_from_file_source = pandas.to_datetime(content[date_column], dayfirst=True).max(axis=0)

    # if oldest sourcefile entry is larger than newest entry from database continue
    # else, abort
    # This is actually not a good way to import data, as I need to remember exactly the latest import timeframe.
    # For now its OK, but it better to check during import, if it is a duplicate and only insert in DB if not.
    if oldest_from_file_source > pandas.to_datetime(newest_from_db):
        # Continue processing the import file

        print("Data is new")
        # swapping , to . in amount col
        new_content = MyContent.ger_to_us(content, ger_to_us_col)

        # add column with hash and add as as column with index sourcelength
        # This makes sure, that it is definitely a new column
        # The data can be accessed with the source length for the original file
        hashed_content = MyContent.add_hash_pandas(new_content, sourcelength)

        # add column with value = unknown
        # Pandas column number is the sourcelength plus one to make a new dedicated column
        hashed_content[sourcelength+1] = "Unknown"

        myDB.store_finance_data_pandas(hashed_content, source)

    else:
        print('Some Datasets have already been imported. Select a sourcefile which does not overlap!')
        exit(99)
