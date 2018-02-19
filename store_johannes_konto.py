import store_transactions_pandas

#location where the file is on the file system
location = r'/Users/johanneshettig/OneDrive/Johannes files/Python/Finance_project/'
# Name of sourcefile on the file system
sourcefile = "Konto_Johannes.csv"
# Type of the sourcefile
source = 'dkbkonto'
# user ID
user_id = 1

store_transactions_pandas.processtransfile(location,sourcefile,source,user_id)
