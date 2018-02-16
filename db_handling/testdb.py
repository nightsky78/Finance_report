import db

testdb = db.Db_handler_user('Finance', "nightsky78","Wolfpack",\
                       "johanneshettigdb.cvadegidr7b8.ap-northeast-1.rds.amazonaws.com",\
                '5432', '1' )

# testdb.createnewdb()

# print(testdb.testDBconnection())

content = ['d1c0f51fb7bccefa88064a94d8502b10;21.11.2017;1,75% f\xfcr Auslandseinsatz;-0.08;unknown', \
           '9b0b6cf3424c6ae8c48ced396f52946d;21.11.2017; DIDI CHUXING*1GNSABCR24NHONG KONG;-4.79;unknown']

testdb.store_finance_data(content)
