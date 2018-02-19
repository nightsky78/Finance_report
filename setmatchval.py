from db_handling import db

sourcename = 'dkbkonto'
name = "TG2"
pattern = 'NaN'
pattern_loc = 1
category_id = 11
user_id = 1


db = db.Db_handler_user('finance', "nightsky78","Wolfpack",\
                       "192.168.56.3",\
                '5432', user_id )

source_id = db.retrieve_source_values(sourcename)


db.store_matching_values(name, source_id[0][6], pattern, pattern_loc, category_id)
