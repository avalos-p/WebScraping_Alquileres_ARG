import os
from decouple import config
from pathlib import Path


# Database Information # working with .env
DB_USER = config('DB_USER')  
DB_PASS = config('DB_PASS')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')

# Directory
ROOT = Path().resolve().parent
ROOT_CSV = os.path.join(ROOT, 'alquileres/csv')
ROOT_DB = os.path.join(ROOT, 'alquileres/db')
ROOT_CLEARDATA = os.path.join(ROOT, 'alquileres/clear_data')
ROOT_LOGS = os.path.join(ROOT, 'alquileres/logs')

# Scraping
SITE_FIRST = ["parairnos.com"] # Site
SITE_FIRST_PROVINCES = {"cordoba":"https://www.parairnos.com/alquileres-en-cordoba",
                       "buenos-aires":"https://www.parairnos.com/alquileres-en-buenos-aires",
                       "mendoza":"https://www.parairnos.com/alquileres-en-mendoza"} # List of sub-sites
SITE_SECOND = ["argenprop.com"] # Site
SITE_SECOND_PROVINCES = {"cordoba":"https://www.argenprop.com/departamentos/alquiler-temporal/cordoba",
                         "mendoza":"https://www.argenprop.com/departamentos/alquiler-temporal/mendoza-arg",
                         "buenos-aires":"https://www.argenprop.com/departamentos/alquiler-temporal/buenos-aires"}
# Loggers
#LOG_DB = 'Dbconnection' # to do
#LOG_ETL = 'ETLTasks' # to do
#LOG_CFG = 'logging.conf' # to do
