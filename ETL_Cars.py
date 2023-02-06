# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:06:37 2023

@author: Alberto G.
"""

import os
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

#os.chdir("C:\\Users\\USUARIO\\Documents\\GitHub\\NicaSource_Project")

def main():
    '''Función principal.'''
    filename = ".\\datasets\\Car_sales.csv"
    df = _extract(filename)
    df = _clean(df)
    engine = connect_mysql()
    _load(df,engine,'car_Sale')

def connect_mysql(): 
    import os
    from dotenv import load_dotenv
    from mysql.connector import Error
    from sqlalchemy import create_engine

    load_dotenv()
    
    host=os.getenv("HOST")
    database=os.getenv("DATABASE")
    user=os.getenv("USER")
    password=os.getenv("PASSWORD")
    
    try:
        engine = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(user,password,host,database))
        return engine
        logger.info("Connection succesfull")
    except Error as e:
        logger.info("Error while connecting to MySQL", e)
    finally:
        engine.dispose()

    
def _extract(filename):
    """Function to extract the information from the csv file """
    
    #os.chdir("C:\\Users\\USUARIO\\Documents\\GitHub\\NicaSource_Project\\datasets")
    try:
        # Load the csv file car_sales.csv
        df_cars = pd.read_csv(filename, sep=",", encoding='utf8')
        logger.info("csv file loaded")
        return df_cars
    
    except Exception as e:
        logger.info("Error loading the csv file", e)
        
#df_cars = df

def _clean(df_cars):
    """Function to clean and transform the data"""
    
    try:
        pd.options.mode.chained_assignment = None
        """remove rows with missing values"""
        droped_rows = str(df_cars.isnull().sum().sum())
        df_cars = df_cars.dropna()
        logger.info(droped_rows +" rows with missing values was eliminated")
        
        """Convert the column with date information to datetime column"""
        df_cars['Last sale date'] = pd.to_datetime(df_cars.loc[:,'Last sale date'].values.tolist())
        logger.info('Column "Last sale date" convertion to dateformat done!')
        
        """Create the column 'Sale year' """
        df_cars["Sale year"] = df_cars.loc[:,"Last sale date"].dt.strftime('%Y')
        logger.info('Column "Sale year" created!')    
        
        """ Replace the categorical values in the "Car Model" column with numerical values """
        df_cars["Model"] = pd.Categorical(df_cars["Model"]).codes
        logger.info('The Car model column was converted to numerical column')    
        
        """ Set column types"""
        df_cars.dtypes
        df_cars.columns
        
        convert_dict = {
                        '4-year resale value': float,
                        'Manufacturer': str,
                        'Vehicle type': str, 
                        'Price in thousands': float, 
                        'Engine size': float, 
                        'Horsepower': int,
                        'Wheelbase': float, 
                        'Width': float, 
                        'Length': float, 
                        'Curb weight': float, 
                        'Fuel capacity': float,
                        'Fuel efficiency': int,  
                        'Sale year': int
                        }
        df_cars = df_cars.replace('.',0)
        df_cars = df_cars.astype(convert_dict)
        logger.info("Data cleaned!")
        return df_cars
        
    except Exception as e:
        logger.info("Error cleaning the data ", e)


def _load(df, engine, tbl_name):
    """Function to load the data into mysql table"""
    
    tbl_name=tbl_name.lower()
    try:
        df.to_sql(
            name=tbl_name,
            con=engine,
            if_exists='replace',
            index=False
        )
        logger.info("table loaded into DataBase sucessfull!")
        
    except Exception as e:
        logger.info("Error loading the data ", e)
    finally:
        engine.dispose()

if __name__ == '__main__':
    main()