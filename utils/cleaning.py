import pandas as pd
import logging
from unidecode import unidecode
import datetime
from config.cfg import PATH_CLEARDATA


from config.cfg import PATH_LOGS,LOG_TASKS,LOG_CFG
from utils.logger import create_logger_from_file,get_logger
create_logger_from_file(LOG_CFG) # logger from .conf file
logger = get_logger(LOG_TASKS) # logger name 

date = datetime.datetime.now()
date_formatted = date.strftime("%d-%m-%Y")

def cleaning_letters(column: pd.Series) -> pd.Series:
    logger.info('Cleaning letters...') # this will clean all the things that are not letters or numbers
    if not isinstance(column, pd.Series):
        raise ValueError('Error: This function works with pandas series - columns')
    column = column.apply(lambda x: unidecode(x) if pd.notnull(x) else x)
    column = column.str.lower()
    column = column.str.replace('[^a-z0-9\s]+', '', regex=True).str.strip()
    return column

def keep_numbers_only(column: pd.Series) -> pd.Series:
    logger.info('Keeping numbers only...') # this will keep just numbers
    if not isinstance(column, pd.Series):
        raise ValueError('Error: This function works with pandas series - columns')
    column = column.astype(str)  # Convert to strings for manipulation
    column = column.str.replace(r'\.', '', regex=True)  # Remove decimal points
    column = column.str.replace(r'[^\d]', '', regex=True)  # Remove non-digits
#   column = column.apply(lambda x: str(x))  # Changes values to str
#    column = column.str.replace('[^0-9]+', '', regex=True)
#    column = pd.to_numeric(column, errors='coerce') # Just in case I want to change empty for NaN
    return column


def number_of_dayss(column: pd.Series) -> pd.Series:
    logger.info('Changing to number of days...') # this will change the days in text to numbers 
    if not isinstance(column, pd.Series):
        raise ValueError('Error: This function works with pandas series - columns')
    
    column = column.replace('por día', '1').replace('por mes', '30').replace('por dia', '1')
    column = column.replace('por quincena', '15').replace('por semana', '7')
    return column


def data_cleaner(file: pd.DataFrame) -> pd.DataFrame :
    logger.info('Cleaning data...') # the data cleaner is using cleaning functions
    if not isinstance(file, pd.DataFrame):
        raise ValueError('Error: File must be pandas DataFrames.')
    file['name'] = cleaning_letters(file['name'])
    file['price'] = keep_numbers_only(file['price'])

    file['days'] = number_of_dayss(file['days'])
    file['days'] = keep_numbers_only(file['days'])

#    file['rooms'] = keep_numbers_only(file['rooms'])
    file['bathrooms'] = keep_numbers_only(file['bathrooms'])
    file['capacity'] = keep_numbers_only(file['capacity'])
    if file['rooms'].dtype == 'float64':
    	file['rooms']= pd.to_numeric(file['rooms'], errors='coerce').dropna().astype(int)
    else:
    	file['rooms'] = keep_numbers_only(file['rooms'])

    return file


def append_data(file1: pd.DataFrame,file2:pd.DataFrame) -> pd.DataFrame :
    logger.info('Appending data...')
    if not isinstance(file1, pd.DataFrame) or not isinstance(file2, pd.DataFrame):
        raise ValueError('Error: Both files must be pandas DataFrames.')
    #file1 = file1.append(file2, ignore_index=True)
    #file1.to_csv(f'clean_data/alquileres_clean{date_formatted}.csv')
    result = pd.concat([file1, file2], axis=0, ignore_index=True)
    result.to_csv(f'{PATH_CLEARDATA}/alquileres_clean{date_formatted}.csv')
    return result # The idea is to apply this function using old structure

def clean_websites(file: pd.DataFrame) -> pd.DataFrame :
    logger.info('Websites removing...')
    if not isinstance(file, pd.DataFrame):
        raise ValueError('Error: File must be pandas DataFrames.')
    file = file.drop(columns=['site'])
    file.to_csv(f'{PATH_CLEARDATA}/alquileres_clean{date_formatted}.csv')
    return  # Important to NOT run this function, this is just for sharing data purposes 
    


