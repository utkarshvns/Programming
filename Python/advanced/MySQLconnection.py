# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:43:19 2022

@author: utkar
"""

# Mysql connection


# pip install mysql-connector

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="mysql4uy",database="telusko")

mycursor = mydb.cursor()


mycursor.execute("select * from student")

# result = mycursor.fetchall()
result = mycursor.fetchone ()

for i in result:
    print(i)