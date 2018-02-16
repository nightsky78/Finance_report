from db_handling import db

sourcename = 'dkbkredit'
name = "Phuket"
pattern = 'PHUKET'
pattern_loc = 1
category_id = 8 
user_id = 1


db = db.Db_handler_user('Finance', "nightsky78","Wolfpack",\
                       "johanneshettigdb.cvadegidr7b8.ap-northeast-1.rds.amazonaws.com",\
                '5432', user_id )

source_id = db.retrieve_source_values(sourcename)


db.store_matching_values(name, source_id[0][6], pattern, pattern_loc, category_id)
