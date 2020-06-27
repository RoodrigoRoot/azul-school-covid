# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pprint
import logging
import psycopg2
 
logging.basicConfig(
    level=logging.DEBUG
)
 
class Covid19Pipeline(object):
 
    def connection_db(self):
       try:
           connection = psycopg2.connect(
           user="root",
           password="forever11",
           host="localhost",
           database="covid19"
           )
           return connection
       except Exception as e:
           logging.debug("Problems with connection db", e)
           return 0
 
    def insert_values(self, con, item):
       try:
           i = 0
           cur = con.cursor()
           for query in item["countrie"]:   
               postgres_insert_query = """ INSERT INTO data(COUNTRIE, CASES, DEATHS) VALUES (%s, %s, %s)"""
               cur.execute(postgres_insert_query, (item["countrie"][i],
                                                    item["cases"][i],
                                                    item["deaths"][i]))
               i = i+1
           con.commit()
           logging.debug("Record inserted successfully into data table")
           return True
       except Exception as e:
           logging.debug("It's not possible insert data in the table", e)
           return 0
 
    def DB(self, item):
       try:
           con = self.connection_db()
           self.insert_values(con, item)
           logging.debug("Data Stored")
       except (Exception, psycopg2.Error) as e:
           logging.debug("Problems with DB", e)


    def process_item(self, item, spider):
        
        values = item['values']
        cases = []
        deaths = []
        for x in range(0, len(values), 2):
            cases.append(values[x])
        
        for x in range(1, len(values),2):
            deaths.append(values[x])
        
        item['cases'] = cases
        item['deaths'] = deaths
        
        self.DB(item)
        return item
