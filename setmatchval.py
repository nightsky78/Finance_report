from db_handling import db
import configparser

source_config = configparser.ConfigParser()
configfilepath = r'../FinanceSource.config'
source_config.read(configfilepath)

sourcename = source_config.get('fileconf2', 'sourcetype')

print('Adding matching value for source: {0}'.format(sourcename))

name = "Auszug1"
pattern = 'MALERBETRIEB'
pattern_loc = 1
category_id = 16
user_id = 1


db = db.Db_handler_user(user_id)

source_id = db.retrieve_source_values(sourcename)


db.store_matching_values(name, source_id[0][6], pattern, pattern_loc, category_id)
