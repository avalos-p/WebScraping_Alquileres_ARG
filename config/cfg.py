import os
from decouple import config
from pathlib import Path


# Database Information # working with .env.
DB_USER = config('DB_USER')  
DB_PASS = config('DB_PASS')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')

# Directory
ROOT = Path().resolve().parent
PATH_CSV = os.path.join(ROOT, 'alquileres/csv')
PATH_DB = os.path.join(ROOT, 'alquileres/db')
PATH_CLEARDATA = os.path.join(ROOT, 'alquileres/clean_data')
PATH_LOGS = os.path.join(ROOT, 'alquileres/logs')

# Scraping
PARAIRNOS_WEBSITE = ["parairnos.com"] # Site
PARAIRNOS_PROVINCES = {"cordoba":"https://www.parairnos.com/alquileres-en-cordoba",
                       "buenos-aires":"https://www.parairnos.com/alquileres-en-buenos-aires",
                       "mendoza":"https://www.parairnos.com/alquileres-en-mendoza"} # List of sub-sites
ARGENPROP_WEBSITE = ["argenprop.com"] # Site
ARGENPROP_PROVINCES = {"cordoba":"https://www.argenprop.com/departamentos/alquiler-temporal/cordoba",
                         "mendoza":"https://www.argenprop.com/departamentos/alquiler-temporal/mendoza-arg",
                         "buenos-aires":"https://www.argenprop.com/departamentos/alquiler-temporal/buenos-aires"}
                                        


# Loggers
#LOG_DB = 'Dbconnection' # to do
LOG_TASKS = 'Tasks' # Name of logger
LOG_CFG = 'logging.conf' # Name of conf file
