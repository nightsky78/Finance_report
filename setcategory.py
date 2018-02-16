from db_handling import db


category = 'Urlaub'
description = 'Urlaubskosten'
user_id = 1


db = db.Db_handler_user('Finance', "nightsky78","Wolfpack",\
                       "johanneshettigdb.cvadegidr7b8.ap-northeast-1.rds.amazonaws.com",\
                '5432', user_id )

db.store_category(category, description)
