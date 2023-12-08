import PET
# technically i dont have to import below its just vscode is highlighting pandas and annoys me
import config
from config import *


@PET.load_to_database
def process_data(df):
    try:
        for col in df.columns:
            # Check if the column is numeric
            if pd.api.types.is_numeric_dtype(df[col]):
                # Convert to numeric and replace null values with 0
                # (sidenote: in my case for now the data is good to fill with 0,
                # if you like you can fill with mean to preserve or minimize distribution)
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        df = df.drop_duplicates()
        # Remove HTML tags from all columns
        df.replace(regex=r'<.*?>|<\/.*?>|<.*?\/?>', value='', inplace=True)
        # removes Special  characters
        df.replace(regex=r'[^a-zA-Z0-9\s]', value='', inplace=True)
    except Exception as e:
        # prints error for debugging
        print(f"An error occurred: {str(e)}")
    return df
