import os
import  sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()


host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db,
        )
        logging.info("Connection Established", mydb)
        query = "Select * from StudentsPerformance"
        df = pd.read_sql_query(query, mydb)
        return df

    except Exception as ex:
        raise CustomException(ex, sys)
    



