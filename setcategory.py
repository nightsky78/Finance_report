from db_handling import db


category = 'Utilities'
description = 'Strom, Wasser, Heizung'
user_id = 1


db = db.Db_handler_user('finance', "nightsky78","Wolfpack",\
                       "192.168.56.3",\
                '5432', user_id )

db.store_category(category, description)
