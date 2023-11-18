import pandas as pd
from unidecode import unidecode

def cleaning_names(column: pd.Series) -> pd.Series:
    # name cleaning
    column = column.apply(lambda x: unidecode(x) if pd.notnull(x) else x)
    column = column.str.lower()  # O file['name'] = file['name'].str.upper()
    column = column.str.replace('[^a-zA-Z0-9\s]+', '', regex=True).str.strip()
    return column

def cleaning_prices(column: pd.Series) -> pd.Series:
   # price cleaning
    column = column.str.replace('\n', '').str.strip() # TO DO: USD CONVERTION
    return column

def cleaning_days(column: pd.Series) -> pd.Series:
    # days cleaning
    column = column.replace('por día', '1').replace('por mes', '30')
    column = column.replace('por quincena', '15').replace('por semana', '7')
    return column

def cleaning_rooms(column: pd.Series) -> pd.Series:
    # rooms cleaning
    column = column.str.replace('\n', '').str.replace('dorm.','').str.strip()
    return column

def cleaning_bathrooms(column: pd.Series) -> pd.Series:
    # bathrooms cleaning
    column = column.str.replace(r'\n', '').str.replace('baños','').str.replace('baño','').str.strip()

    return column


# capacity cleaning