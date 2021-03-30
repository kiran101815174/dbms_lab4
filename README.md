# dbms_lab4
DBMS Lab
ENC8
Lab Assignment-4
VIJAYPAL SINGH RATHOR
•
Mar 24
100 points
Due Tomorrow

DBMS Lab Assignment 4.docx
Word
Class comments
Your work
Assigned
Private comments
Page3/3
For this lab you have to create a Banking Enterprise Database. This database keeps track of
bank customers, also allow them to borrow loan and deposit money in their account of
different branches. ER diagram of this database is given as:

Information
stored in a
database
consisting of 6
Tables:
1. BRANCH: stores
description of
each branch of
the bank
2. ACCOUNT:
stores information
about accounts
3. CUSTOMER:
stores information

about customers
4. LOAN: stores loans details for each customers
5. DEPOSITOR: stores information about which customer owns which account
6. BORROWER: associates customer with loan taken
Task - Table Creation
Create all the necessary tables with the columns name described by the ER diagram. Choose the
appropriate data types for the columns as per the information given.
Table Details
Six tables of Banking Enterprise Database:
◦BRANCH, ACCOUNT, CUSTOMER, LOAN, DEPOSITOR, and BORROWER
The columns where NULL values are allowed are stated explicitly or else the column
should not allow any NULL values.
Descriptions of tables is given as follows:
CUSTOMER Table Example

CUSTOMER_NAME Unique customer name associated with an account. VARCHAR(15). PRIMARY
KEY.
CUSTOMER_STREET Name of the street in which customer lives. VARCHAR(15). NULL allowed.
CUSTOMER_CITY Name of the city in which customer lives. VARCHAR(15).
Syntax – Customer TABLE
CREATE TABLE customer
(customer_nameVARCHAR(15) NOT NULL,
customer_streetVARCHAR(15) ,
customer_cityVARCHAR(15) NOT NULL,
PRIMARY KEY(customer_name)
);
BRANCH Table
BRANCH_NAME Unique branch name for different branches of the bank. VARCHAR(15). PRIMARY
KEY.
BRANCH_CITY Name of the city in which branch is located. VARCHAR(15).
ASSETS The bank monitors the assets of each branch. INTEGER(8).

ACCOUNT Table
ACCOUNT_NUMBER Unique account number in a bank branch. INTEGER(8). PRIMARY KEY.
BRANCH_NAME Brach name in which the account is opened. VARCHAR(15), FOREIGN KEY
to BRANCH table.
BALANCE Keeps track of the balance left in the account. INTEGER(8).
DATE The most recent date on which the account was accessed by the customer.
DATE. Stores year, month, and day values (yyyy-mm-dd)

LOAN Table
LOAN_NUMBER A loan originates at a particular branch and can be held by one or more
customers.
A loan is identified by a unique loan number. INTEGER(8). PRIMARY KEY.
BRANCH_NAME Brach name in which the account is opened. VARCHAR(15), FOREIGN KEY to
BRANCH table.

AMOUNT Keeps track of the loan amount taken by a customer. INTEGER(8).

DEPOSITOR Table
CUSTOMER_NAME Unique customer name associated with an account. VARCHAR(15). FOREIGN KEY
to CUSTOMER table.
ACCOUNT_NUMBER Unique account number in a bank branch. INTEGER(8).FOREIGN KEY to
ACCOUNT table.
BORROWER Table
CUSTOMER_NAME Unique customer name associated with an account. VARCHAR(15). FOREIGN KEY
to CUSTOMER table.
LOAN_NUMBER A loan is identified by a unique loan number. INTEGER(8). FOREIGN KEY to LOAN
table.
Page 1 of 3Lab Assignment 4UCS 310 DBMSFor this lab you have to create a Banking Enterprise Database. This database keeps track ofbank customers, also allow them to borrow loan and deposit money in their account ofdifferent branches. ER diagram of this database is given as:Informationstored in adatabaseconsisting of 6Tables:1. BRANCH: storesdescription ofeach branch ofthe bank2. ACCOUNT:stores informationabout accounts3. CUSTOMER:stores informationabout customers4. LOAN: stores loans details for each customers5. DEPOSITOR: stores information about which customer owns which account6. BORROWER: associates customer with loan takenTask - Table CreationCreate all the necessary tables with the columns name described by the ER diagram. Choose theappropriate data types for the columns as per the information given.Table DetailsSix tables of Banking Enterprise Database:◦BRANCH, ACCOUNT, CUSTOMER, LOAN, DEPOSITOR, and BORROWERThe columns where NULL values are allowed are stated explicitly or else the columnshould not allow any NULL values.Descriptions of tables is given as follows:CUSTOMER Table Example
Page 2 of 3CUSTOMER_NAME Unique customer name associated with an account. VARCHAR(15). PRIMARYKEY.CUSTOMER_STREET Name of the street in which customer lives. VARCHAR(15). NULL allowed.CUSTOMER_CITY Name of the city in which customer lives. VARCHAR(15).Syntax – Customer TABLECREATE TABLE customer(customer_nameVARCHAR(15) NOT NULL,customer_streetVARCHAR(15) ,customer_cityVARCHAR(15) NOT NULL,PRIMARY KEY(customer_name));BRANCH TableBRANCH_NAME Unique branch name for different branches of the bank. VARCHAR(15). PRIMARYKEY.BRANCH_CITY Name of the city in which branch is located. VARCHAR(15).ASSETS The bank monitors the assets of each branch. INTEGER(8).ACCOUNT TableACCOUNT_NUMBER Unique account number in a bank branch. INTEGER(8). PRIMARY KEY.BRANCH_NAME Brach name in which the account is opened. VARCHAR(15), FOREIGN KEYto BRANCH table.BALANCE Keeps track of the balance left in the account. INTEGER(8).DATE The most recent date on which the account was accessed by the customer.DATE. Stores year, month, and day values (yyyy-mm-dd)LOAN TableLOAN_NUMBER A loan originates at a particular branch and can be held by one or morecustomers.A loan is identified by a unique loan number. INTEGER(8). PRIMARY KEY.BRANCH_NAME Brach name in which the account is opened. VARCHAR(15), FOREIGN KEY toBRANCH table.
Page 3 of 3AMOUNT Keeps track of the loan amount taken by a customer. INTEGER(8).DEPOSITOR TableCUSTOMER_NAME Unique customer name associated with an account. VARCHAR(15). FOREIGN KEYto CUSTOMER table.ACCOUNT_NUMBER Unique account number in a bank branch. INTEGER(8).FOREIGN KEY toACCOUNT table.BORROWER TableCUSTOMER_NAME Unique customer name associated with an account. VARCHAR(15). FOREIGN KEYto CUSTOMER table.LOAN_NUMBER A loan is identified by a unique loan number. INTEGER(8). FOREIGN KEY to LOANtable.
Find in document
DBMS Lab Assignment 4.docx
Page 3 of 3
