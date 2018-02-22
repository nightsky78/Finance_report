import store_transactions_pandas
import configparser


# read Configfile to determine the source
source_config = configparser.ConfigParser()
configfilepath = r'../FinanceSource.config'
source_config.read(configfilepath)

location = source_config.get('fileconf', 'location')
sourcefile = source_config.get('fileconf', 'sourcefile')
source = source_config.get('fileconf', 'sourcetype')

print ('Reading config file with location: {0} - sourcefile: {1} - sourcetype: {2}'.format(location, sourcefile, source))

# user ID
user_id = 1

store_transactions_pandas.processtransfile(location,sourcefile,source,user_id)
