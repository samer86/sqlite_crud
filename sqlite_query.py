# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:55:30 2021

@author: salem
"""
import sqlite3
from sqlite3 import Error
import pandas as pd
'''CONNECT USING sqlite3 '''
conn = sqlite3.connect('class.db')
cursor = conn.cursor()
print("Opened database successfully")
cursor.close()


class db():
    __query = ''
    results = []
    columns = []
    __data= ''
    __tables = ''
    
    def __init__(self):
        self.query = "SELECT name FROM sqlite_master WHERE type='table';"
        self.__tables = self.data()
    
    @property
    def query(self):

        print(self.__query)
        return self.__query
        
    @query.setter
    def query(self,stmt):
        self.__query = stmt
        #Create cursor and send stmt query to database
        try:
            cursor = conn.cursor()
            res = cursor.execute(stmt)
            rows =res.fetchall()
            #Save columns from the query into self.columns
            if isinstance(cursor.description,tuple):
                self.columns= [tuple[0] for tuple in cursor.description]
                # print(self.columns)
            else:
                self.columns=[]
                # print(self.columns)
            '''save results into self.results using genertor method!'''
            results = [row for row in rows]
            if len(results)> 0 :
                self.results = results
            else:
                self.results = 'There are no data to show!'
            
            '''
            1. Make a dataframe from (rows and columns) if rows has data.
            2. Else assign (there are no data) to self.__data
                a. Check if there are columns, if yes its an empty dataframe
                    Then Query Successfully commer.
                b. Else just print the dataFrame.
            '''
            
            if len(results)>0:
                self.__data= pd.DataFrame(rows,columns=self.columns)
                print(self.__data.to_string(index=False))
            else:
                self.__data = 'There are no data to show!'
                if len(self.columns) == 0:
                    print('Query Successfully Finished!')
                else :
                    # print('hello from else' )
                    self.__data = pd.DataFrame(rows,columns=self.columns)
                    print(pd.DataFrame(rows,columns=self.columns))

            #Closing connection: cursor
            cursor.close()
            
        except Error as e :
            print(e)


    def data(self):
        return self.__data
        
    def commit(self):
        conn.commit()
        
        # return 'There are no data to show!'
    @property
    def tables(self):
        # print('This is tables getter')
        self.query = "SELECT name FROM sqlite_master WHERE type='table';"
        self.__tables = self.data()
     
    @tables.setter
    def tables(self,stmt):
        pass


db = db()

# while True:
#     db.query = input('Enter your query:\n')






