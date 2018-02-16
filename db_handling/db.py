import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Db_handler_user:
    def __init__(self, dbname, user, password, host, port, user_ID):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.user_ID = user_ID

    def testDBconnection(self):
        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()
        
        cur.execute('select * from test')
        return cur.fetchall()

    def createnewdb(self):
        con = psycopg2.connect(dbname='postgres', user=self.user, host=self.host, password=self.password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        cur = con.cursor()
        cur.execute('CREATE DATABASE ' + self.dbname)
#        print(cur.fetchall())

    def deletedb(self):
        con = psycopg2.connect(dbname='postgres', user=self.user, host=self.host, password=self.password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        cur = con.cursor()
        cur.execute('DROP DATABASE ' + self.dbname)
#        print(cur.fetchall())

    def store_matching_values(self, name, source_id, pattern, pattern_loc_id, category_id):

        self.name = name
        self.source_id = source_id
        self.pattern = pattern
        self.pattern_loc_id = pattern_loc_id
        self.category_id = category_id
        
        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        query =  "INSERT INTO matchval (name, source_id, pattern, pattern_loc_id, category_id, user_id) VALUES (%s, %s, %s, %s, %s, %s);"
        data = (self.name, self.source_id, self.pattern, self.pattern_loc_id, self.category_id, self.user_ID )

        cur.execute(query, data)

        con.commit()
        con.close()

    def retrieve_matching_values(self, source_ID):
        self.source_ID = source_ID

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        query =  "SELECT pattern, pattern_location FROM matching WHERE source_id=%s AND user_id=%s;"
        data = (self.source_ID, self.user_ID)

        cur.execute(query, data)
 
        return cur.fetchall()

    def retrieve_all_matching_values(self):

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        cur.execute("SELECT name, pattern, pattern_loc_id, category_id, source_id FROM matchval WHERE user_id={0};".format(self.user_ID))

        return cur.fetchall()

    def store_source_values(self, name, description, delimiter, length, date_column, \
                            subject_column, amount_column):
        self.name = name
        self.description = description
        self.delimiter = delimiter
        self.length = length
        self.date_column = date_column
        self.subject_column = subject_column
        self.amount_column = amount_column

        
        
        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        query =  "INSERT INTO source (name, description, delimiter, length, date_column, subject_column, amount_column, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (self.name, self.description, self.delimiter, self.length, self.date_column, subject_column, amount_column, self.user_ID )

        cur.execute(query, data)

        con.commit()
        
        con.close()

    def retrieve_source_values(self, name):
        self.name = name

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        cur.execute("SELECT name, delimiter, length, date_column,\
                            subject_column, amount_column, source_id FROM sourcefile WHERE name='{0}' \
                            and user_ID={1};".format(self.name,self.user_ID))
        return cur.fetchall()

    def update_transaction_category(self, category_id, pattern, pattern_loc, source_id):
        self.category_id = category_id
        self.pattern = pattern
        self.source_id = source_id
        self.pattern_loc = pattern_loc

        print(self.category_id)
        print(self.pattern)
        print(self.source_id)
        print(self.pattern_loc)
        
        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()
        print("update transactions set category_id = {0} where {1} like '%{2}%' \
                and source_id = {3} and user_id = {4}".format(self.category_id, self.pattern_loc, self.pattern, self.source_id, self.user_ID))
        cur.execute("update transactions set category_id = {0} where {1} like '%{2}%' \
                and source_id = {3} and user_id = {4}".format(self.category_id, self.pattern_loc, self.pattern, self.source_id, self.user_ID))
        
        con.commit()
        
        con.close()

    def store_category(self, category, description):
        self.category = category
        self.description = description
      
        
        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        query =  "INSERT INTO categories (category, description, user_id) VALUES (%s, %s, %s);"
        data = (self.category, self.description, self.user_ID )

        cur.execute(query, data)

        con.commit()
        
        con.close()


    def retrieve_category(self, name):
        self.name = name

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        cur.execute("SELECT name, delimiter, length, date_column,\
                            subject_column, amount_column, source_id FROM sourcefile WHERE name='{0}' \
                            and user_ID={1};".format(self.name,self.user_ID))
        return cur.fetchall()         
        
    def store_finance_data(self, content, source):
        self.content = content
        self.source = source

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        cur.execute("SELECT source_id FROM sourcefile WHERE name = '{0}';".format(self.source))
        source_id = cur.fetchall()[0]
     
        for line in content:
            splitline = line.split(';')
            print("Entering: {0}".format(splitline))
#            print(splitline[1])
#            print(splitline[2])
#            print(splitline[3])
#            print(splitline[4])
            
            cur.execute("SELECT cat_id FROM categories WHERE category = '{0}';".format(splitline[4]))
            category_id = cur.fetchall()[0]


            query =  "INSERT INTO transactions (hash, date, subject, amount, category_id, user_id, source_id) VALUES (%s, to_date(%s, 'DD.MM.YYY'), %s, %s, %s, %s, %s);"
            data = (splitline[0], splitline[1], splitline[2], splitline[3], category_id, self.user_ID, source_id)
            cur.execute(query, data)

        con.commit()
        
        con.close()
        
             








             
