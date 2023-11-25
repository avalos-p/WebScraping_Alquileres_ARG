import pandas as pd
from unidecode import unidecode


def cleaning_letters(column: pd.Series) -> pd.Series:
    if not isinstance(column, pd.Series):
        raise ValueError('Error: This function works with pandas series - columns')
    column = column.apply(lambda x: unidecode(x) if pd.notnull(x) else x)
    column = column.str.lower()
    column = column.str.replace('[^a-z0-9\s]+', '', regex=True).str.strip()
    return column

def keep_numbers_only(column: pd.Series) -> pd.Series:
    if not isinstance(column, pd.Series):
        raise ValueError('Error: This function works with pandas series - columns')
    column = column.apply(lambda x: str(x))  # Changes values to str
    column = column.str.replace('[^0-9]+', '', regex=True)
#    column = pd.to_numeric(column, errors='coerce') # Just in case I want to change empty for NaN
    return column

def number_of_dayss(column: pd.Series) -> pd.Series:
    if not isinstance(column, pd.Series):
        raise ValueError('Error: This function works with pandas series - columns')
    
    column = column.replace('por día', '1').replace('por mes', '30').replace('por dia', '1')
    column = column.replace('por quincena', '15').replace('por semana', '7')
    return column