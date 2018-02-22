import store_transactions_pandas
import configparser

# read Configfile to determine the source
source_config = configparser.ConfigParser()
configfilepath = r'../FinanceSource.config'
source_config.read(configfilepath)

location = source_config.get('fileconf2', 'location')
sourcefile = source_config.get('fileconf2', 'sourcefile')
source = source_config.get('fileconf2', 'sourcetype')

# user ID
user_id = 1

# call DB storage procedures
store_transactions_pandas.processtransfile(location,sourcefile,source,user_id)
