import store_transactions


location = r'C:\Users\Johannes\OneDrive\Johannes files\Python\FSND-Virtual-Machine\vagrant\Finance'
sourcefile = "4748________0595.csv"
source = 'dkbkredit2'
user_id = 1
exclusions = "Wertstellung"


store_transactions.processtransfile(location,sourcefile,source,exclusions,user_id)
