## Nicasourse ETL Project
**Create By:** _Alberto García_

Import, clean, and transform a car sales CSV files, then load it into MySQL database.

## Setup your environment:

## 1. Download & install Python to run the program.
- https://www.python.org/downloads/
- https://www.journaldev.com/30076/install-python-windows-10
- https://www.howtogeek.com/197947/how-to-install-python-on-windows/

## 2. Install the required packages
- pip install -U pandas
- pip install logging
- pip install dotenv
- pip install -U sqlalchemy
- pip install -U mysql-connector
- pip install PyMySQL

## 3. Download & Install the MySQL Community database software.
- https://dev.mysql.com/downloads/mysql/
- https://www.sqlshack.com/how-to-install-mysql-database-server-8-0-19-on-windows-10/
- https://www.onlinetutorialspoint.com/mysql/install-mysql-on-windows-10-step-by-step.html
- Finally, you have to create "Nicasource" Database with this script:

  > CREATE DATABASE IF NOT EXISTS Nicasource;
  
## 4. Configure the .env file.
It's important to setup the connection variables (host, user, password, database) and save the file to connect with mysql database

## 5. In the 'datasets' folder is located de CSV file named 'car_sales.scv'.
## 6. The 'ETL_Cars.py' script contains the following functions:
  - **_Extract() Function:** This function have a filename paramenter to extract the data from the file and load it into a dataframe.
  - **_Clean() Function:** This function have a dataframe parameter to clean, tranform an return the dataframe.
  - **connect_mysql() Function:** This function read the enviroment variables and connects to mysql database. Finally return a engine variable.
  - **_load() Function:** this function load the dataframe into a mysql table. Have a dataframe, the conection and the table name parameters.

## 7. To run the ETL_Cars.py script follow these steps:
  - **1.** Open the terminal or command prompt.
  - **2.** Navigate to the directory where the script is located.
  - **3.** Type "python scriptname.py" (without quotes) and press Enter.
>Note: Replace "scriptname" with the actual name of your script. If the Python executable is not in your system PATH, you may need to specify the full path to the Python executable, such as "/usr/bin/python scriptname.py"
