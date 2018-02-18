from db_handling import db
from _Archive import file


def processtransfile(location,sourcefile,source,user_id):

    myfile = file.File(sourcefile, location)

    mycontent = myfile.get_cleaned_content()
    testdb = db.Db_handler_user('finance', "nightsky78","Wolfpack",\
                       "192.168.2.221",\
                '5432', user_id )

    mysource = testdb.retrieve_source_values(source)
    sourcelength = mysource[0][2]
    sourcedelimiter = mysource[0][1]
    ger_to_us_col = mysource[0][5]
    incl_column = [mysource[0][3],mysource[0][4],mysource[0][5]]
    i = 0
    excl_column = []
    for i in range (0, sourcelength):
        if i not in incl_column:
           excl_column.append(i)
        i = i+1
            
    cleancontent = myfile.get_structured_content(mycontent, sourcedelimiter ,sourcelength ,\
                                                 excl_column,exclusions, ger_to_us_col)

    hashedcontent = myfile.add_hash(cleancontent)

    # matching stub
    new_hashed_content = []
    for line in hashedcontent:
        line = line + ';Unknown'
        new_hashed_content.append(line)


    testdb.store_finance_data(new_hashed_content, source)


