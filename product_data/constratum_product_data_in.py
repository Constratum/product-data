import pandas as pd
from . import data
import importlib.resources


def convert_df_to_python_types(df):
    converted_df = pd.DataFrame()
    
    for column in df.columns:
        dtype = df[column].dtype
        if dtype == 'object':
            converted_df[column] = df[column].astype(str)
        elif 'datetime' in str(dtype):
            converted_df[column] = df[column].astype('datetime64[ns]')
        elif 'int' in str(dtype):
            converted_df[column] = df[column].astype(int)
        elif 'float' in str(dtype):
            converted_df[column] = df[column].astype(float)
        else:
            converted_df[column] = df[column]
    
    return converted_df

def get_df_from_file_name(filename):
    """Return a dataframe containing data from specified csv filename"""

    path = importlib.resources.open_text(data, filename)
    df = pd.read_csv(path) 
    standard_df = convert_df_to_python_types(df)
    return standard_df
