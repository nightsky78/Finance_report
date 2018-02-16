import sys
from db_handling import db

# sys.path.append("/vagrant/Finance/filehandling")

from filehandling import file

# import file
import time

#location = r'/vagrant/Finance'
location = r'C:\Users\Johannes\OneDrive\Johannes files\Python\FSND-Virtual-Machine\vagrant\Finance'
source = 'dkbkredit'

# Konto
#myfile = file.File("15908965.csv",r"C:\Users\q204249\Desktop\Python\Finance")

#Kreditkarte
myfile = file.File("4748________0796.csv", location)

testdb = db.Db_handler_user('Finance', "nightsky78","Wolfpack",\
                       "johanneshettigdb.cvadegidr7b8.ap-northeast-1.rds.amazonaws.com",\
                '5432', '1' )

mycontent = myfile.get_cleaned_content()
#        for line in mycontent:
#            print(line)

#Konto
#excl_column = [0,2,5,6,8,9,10,11]
#ger_to_us_col = [7]
#exclusions = ["Wertstellung"]
#cleancontent = myfile.get_structured_content(mycontent, ";", 12, excl_column, exclusions, ger_to_us_col)

#Kreditkarte
mysource = testdb.retrieve_source_values(source)
sourcelength = mysource[0][2]
sourcedelimiter = mysource[0][1]
ger_to_us_col = mysource[0][5]
print('Amount: {0}'.format(ger_to_us_col))

incl_column = [mysource[0][3],mysource[0][4],mysource[0][5]]
i = 0
excl_column = []
for i in range (0, sourcelength):
    if i not in incl_column:
       excl_column.append(i)
    i = i+1
        
exclusions = "Wertstellung"
cleancontent = myfile.get_structured_content(mycontent, sourcedelimiter ,sourcelength ,\
                                             excl_column,exclusions, ger_to_us_col)

hashedcontent = myfile.add_hash(cleancontent)

# matching stub
new_hashed_content = []
for line in hashedcontent:
    line = line + ';unknown'
    new_hashed_content.append(line)
    
#for line in new_hashed_content:
#    print(line)


testdb.store_finance_data(new_hashed_content, source)
	
#time.sleep(5)	
#input('Press Enter to continue')
