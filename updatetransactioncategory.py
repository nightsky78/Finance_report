from db_handling import db
import configparser

source_config = configparser.ConfigParser()
configfilepath = r'../FinanceSource.config'
source_config.read(configfilepath)

sourcename = source_config.get('fileconf2', 'sourcetype')

user_id = 1


db = db.Db_handler_user(user_id)

source_id = db.retrieve_source_values(sourcename)
print(source_id[0][6])

#Hole alle Zeilen aus matchval
matchval = db.retrieve_matching_values(source_id[0][6])
print(matchval)

#fuer jeden zeile execute eine update transaction category
for line in matchval:
    db.update_transaction_category(line[3], line[1], 'subject', line[4])
