import os
from decouple import config
from pathlib import Path

<<<<<<< HEAD
# Database Information # working with .env
=======

# Database Information # working with .env.
>>>>>>> task/database
DB_USER = config('DB_USER')  
DB_PASS = config('DB_PASS')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')

# Directory
<<<<<<< HEAD
#ROOT = Path(__file__).resolve().parent.parent
ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.dirname(ROOT)
PATH_CSV = os.path.join(ROOT, 'csv')
PATH_CSV = os.path.abspath(PATH_CSV)

#PATH_CSV = os.path.join(ROOT, 'alquileres/csv')
#ROOT = os.path.abspath(os.path.dirname(__file__))

=======
#ROOT = Path().resolve().parent
ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.dirname(ROOT)

PATH_CSV = os.path.join(ROOT, 'csv')
>>>>>>> task/database
PATH_DB = os.path.join(ROOT, 'db')
PATH_CLEARDATA = os.path.join(ROOT, 'clean_data')
PATH_LOGS = os.path.join(ROOT, 'logs')

# Scraping
PARAIRNOS_WEBSITE = ["parairnos.com"] # Site
<<<<<<< HEAD
=======
ARGENPROP_WEBSITE = ["argenprop.com"] # Site

>>>>>>> task/database

PARAIRNOS_PROVINCES = {"cordoba":"https://www.parairnos.com/alquileres-en-cordoba",
                       "buenos-aires":"https://www.parairnos.com/alquileres-en-buenos-aires",
                       "mendoza":"https://www.parairnos.com/alquileres-en-mendoza"} # List of sub-sites
<<<<<<< HEAD
ARGENPROP_WEBSITE = ["argenprop.com"] # Site

=======
>>>>>>> task/database
ARGENPROP_PROVINCES = {"cordoba":"https://www.argenprop.com/departamentos/alquiler-temporal/cordoba",
                         "mendoza":"https://www.argenprop.com/departamentos/alquiler-temporal/mendoza-arg",
                        "buenos-aires":"https://www.argenprop.com/departamentos/alquiler-temporal/buenos-aires"}
                                        


# Loggers

#LOG_DB = 'Dbconnection' # to do
LOG_TASKS = 'Tasks' # Name of logger
LOG_CFG = 'logging.conf' # Name of conf file
