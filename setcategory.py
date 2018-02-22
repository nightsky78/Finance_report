from db_handling import db


category = 'Utilities'
description = 'Strom, Wasser, Heizung'
user_id = 1


db = db.Db_handler_user(user_id)

db.store_category(category, description)
