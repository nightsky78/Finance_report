import store_transactions


location = r'/Users/johanneshettig/OneDrive/Johannes files/Python/Finance_project'
sourcefile = "4748________0796.csv"
source = 'dkbkredit'
user_id = 1
exclusions = "Wertstellung"


store_transactions.processtransfile(location,sourcefile,source,exclusions,user_id)
