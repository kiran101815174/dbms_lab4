import mysql.connector

db=mysql.connector.connect(
    user="root",
    host="localhost",
    passwd="root",
    database="lab4base"
   )
mycursor=db.cursor()
mycursor.execute("CREATE DATABASE lab4base")
mycursor.execute("CREATE TABLE Customer (customer_name VARCHAR(15) NOT NULL PRIMARY KEY,customer_street VARCHAR(15) NOT NULL, customer_city VARCHAR(15) NOT NULL)")
mycursor.execute("CREATE TABLE BRANCH (BRANCH_NAME VARCHAR(15) PRIMARY KEY,BRANCH_CITY VARCHAR(15),ASSETS INT(8),UNIQUE KEY branch_name(BRANCH_NAME))")
mycursor.execute("CREATE TABLE ACCOUNT(ACCOUNT_NUMBER INTEGER(8) PRIMARY KEY,BRANCH_NAME VARCHAR(15) ,BALANCE INTEGER(8),date DATE,UNIQUE KEY (ACCOUNT_NUMBER),FOREIGN KEY (BRANCH_NAME) REFERENCES BRANCH(BRANCH_NAME))")
mycursor.execute("CREATE TABLE LOAN(LOAN_NUMBER INTEGER(8) PRIMARY KEY,BRANCH_NAME VARCHAR(15),AMOUNT INTEGER(8),UNIQUE KEY(LOAN_NUMBER),FOREIGN KEY(BRANCH_NAME) REFERENCES BRANCH(BRANCH_NAME)) ")
mycursor.execute("CREATE TABLE DEPOSITOR(customer_name VARCHAR(15),ACCOUNT_NUMBER INTEGER(8),FOREIGN KEY(ACCOUNT_NUMBER) REFERENCES ACCOUNT(ACCOUNT_NUMBER),FOREIGN KEY(customer_name) REFERENCES Customer(customer_name) )")
mycursor.execute("CREATE TABLE BORROWER(customer_name VARCHAR(15),LOAN_NUMBER INTEGER(8),FOREIGN KEY(LOAN_NUMBER) REFERENCES LOAN(LOAN_NUMBER),FOREIGN KEY(customer_name) REFERENCES Customer(customer_name))")