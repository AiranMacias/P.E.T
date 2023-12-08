import config
from config import *
# Create SQLAlchemy engine to connect to PostgreSQL Database
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@localhost:5432/{database}"
)


# a decorator function processes all csv files in data folder(folder should be namned data)
def load_to_database(process_data):
    for file in glob.glob("data/*.csv"):
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(file)
        try:
            df = process_data(df)
        except:
            df.to_sql(file[5:-4], engine, index=False, if_exists='replace')

        print(f'importing {file[5:-4]}')
        # the name is based on the csv file name best avoid adding spaces and special characters
        df.to_sql(file[5:-4], engine, index=False, if_exists='replace')

        print(f'Done importing {file[5:-4]} to PostgreSQL.')


# Close the database connection
engine.dispose()
