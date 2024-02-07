import os
import pandas as pd

import datetime
import time

from config.cfg import ROOT, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME , LOG_CFG, LOG_TASKS 
from sqlalchemy import create_engine, Column, String, Integer, Float, Text, Date, inspect, exc 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()
date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y")

class Alquileres_Table(Base):
    __tablename__ = 'alquileres'

    # Here Im declaring the table and columns 

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Float)
    days = Column(Integer)
    rooms = Column(Integer)
    bathrooms = Column(Integer)
    capacity = Column(Integer)
    date = Column(Date)
    province = Column(String)
    site = Column(String)


'''Functions'''


def create_folder(path):
    # Create folder if doesnt exist
    if not os.path.exists(path):
        os.makedirs(os.path.join(ROOT, 'alquileres', path))

def create_engine_connection():
    # Create engine for database connection.
    # This works with postgresql db

    '''Important'''
    # USER MUST add data to .env  ##

    DB_CONSTRUCTOR= 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
    return create_engine(DB_CONSTRUCTOR, echo=True)


def connection_db():
    # Connect to Postgres database. If it's not working it will retry 5 times.
    # If the tables aren't in the db it creates the table and columns

    retry = 0
    flag = True

    while flag and retry < 5:
        try:
            # Create engine
            engine = create_engine_connection()
            # Connection
            engine.connect()
            insp = inspect(engine)

            # Check if tables exist
            if not insp.has_table('alquileres'):
                print('Table does not exist, creating it')
                Base.metadata.create_all(engine)
                print('Table "alquileres" created.')
                flag = False
                print('Done')
            else:
                print('Table already exists.')
                flag = False
        except SQLAlchemyError:
            retry += 1
            time.sleep(30)
    
    if not flag:
        print('Connected to the database.')
        return engine
    else:
        print('Connection failed after 5 retries.')


def upload_db(path_csv:str, engine):

    dtype_dict = {
    'id': Integer(),
    'name': Text(),
    'price': Float(),
    'days': Integer(),
    'rooms': Integer(),
    'bathrooms': Integer(),
    'capacity': Integer(),
    'date': Date(),
    'province': Text(),
    'site': Text()
    }

    # Using pandas to read csv
    ##df = pd.read_csv(f'clean_data/alquileres_clean{date_formatted}.csv')
    df = pd.read_csv(path_csv)

    df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

    # Rename 'date' to 'yyyy-mm-dd'
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y').dt.date

    # Choosing Tabe
    nombre_tabla = "alquileres"

    # Using pandas SQL method for uploading data to postgres 
    df.to_sql(nombre_tabla, engine, index=False, if_exists='append', dtype=dtype_dict)
    # if_exists='' for append or replace data
    # Si prefieres agregar datos a la tabla existente en lugar de reemplazarla,
    # utiliza if_exists='append' en lugar de 'replace'

    # Closing connection
    engine.dispose()
