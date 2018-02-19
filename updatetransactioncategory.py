from db_handling import db

sourcename = 'dkbkreditJohannes'
user_id = 1


db = db.Db_handler_user('finance', "nightsky78","Wolfpack",\
                       "192.168.56.3",\
                '5432', user_id )

source_id = db.retrieve_source_values(sourcename)
print(source_id[0][6])
#Hole alle Zeilen aus matchval
matchval = db.retrieve_matching_values(source_id[0][6])
print(matchval)
#fuer jeden zeile execute eine update transaction category
for line in matchval:
    db.update_transaction_category(line[3], line[1], 'subject', line[4])
