from db_handling import db
from filehandling import read_csv_pandas


def processtransfile(location,sourcefile,source,user_id):

    # First we need to retrieve the data for the source file

    myDB = db.Db_handler_user('finance', "nightsky78","Wolfpack",\
                       "192.168.56.3",\
                '5432', user_id )

    mysource = myDB.retrieve_source_values(source)
    sourcelength = mysource[0][2]
    sourcedelimiter = mysource[0][1]
    ger_to_us_col = mysource[0][5]
    skiprow = mysource[0][7]
    incl_column = [mysource[0][3], mysource[0][4], mysource[0][5]]

    # Now find the columns to delete with Pandas method
    x = 0
    excl_columns = []
    while x < sourcelength:
        if x not in incl_column:
            excl_columns.append(x)
        x = x + 1

    # getting data back with the pandas file
    MyContent = read_csv_pandas.ReadCsvPandas(sourcefile,location)

    content = MyContent.get_pandas_content(skiprow,excl_columns, sourcedelimiter)

    # swapping , to . in amount col
    new_content = MyContent.ger_to_us(content, ger_to_us_col)

    # add column with hash and add as as column with index sourcelength
    # This makes sure, that it is definitely a new column
    # The data can be accessed with the column number for the original file
    hashed_content = MyContent.add_hash_pandas(new_content, sourcelength)

    # add column with value = unknown
    # Pandas column number is the sourcelength plus one to make a new dedicated column
    hashed_content[sourcelength+1] = "Unknown"

    myDB.store_finance_data_pandas(hashed_content, source)
