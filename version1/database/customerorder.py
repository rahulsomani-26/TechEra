# from _typeshed import NoneType
import sqlite3 as sq

class DatabaseEngine:
    con = sq.connect('masterdb.sql')

    def __init__(self):
        DatabaseEngine.con.execute('create table if not exists USERS(username text,password text)')
        DatabaseEngine.con.execute('create table if not exists CUSTOMER(cust_id int,cust_name text,cust_address text,cust_email text,product text,price float,quantity int)')
        # DatabaseEngine.con.execute('create table if not exists ORDER')
        self.dummy_data()

    def dummy_data(self):
        try:
            DatabaseEngine.con.execute('insert into USERS values(?,?)',('rahul','thisislife'))
            print('Success in creating a new user')
        except Exception as e:
            print(e)


    def dummy_check(self,username,password):
        # checks for the credentials 
        result = DatabaseEngine.con.execute('select * from USERS where username=? and password=?',(username,password)).fetchall()
        for record in result:
            if record[0]=='rahul' and record[1]=='thisislife':
                print('Logged in')
                break            

        else:
            print('Invalid credentials')        


   