from db_handling import db

sourcename = 'dkbkredit2'
user_id = 1


db = db.Db_handler_user('Finance', "nightsky78","Wolfpack",\
                       "johanneshettigdb.cvadegidr7b8.ap-northeast-1.rds.amazonaws.com",\
                '5432', user_id )

source_id = db.retrieve_source_values(sourcename)

#Hole alle Zeilen aus matchval
matchval = db.retrieve_all_matching_values()

#fuer jeden zeile execute eine update transaction category
for line in matchval:
    db.update_transaction_category(line[3], line[1], 'subject', line[4])
