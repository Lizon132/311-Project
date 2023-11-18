import pandas as pd
from sqlalchemy import create_engine

# Create an SQLAlchemy engine for the database connection
engine = create_engine('mysql+mysqlconnector://root:*@localhost/project_311')

# Path to your CSV file
csv_file_path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/correlation_results.csv'

# Column name mapping to match CSV headers with table column names
column_mapping = {
    'SR TYPE 1': 'SR_Type_1',
    'SR TYPE 2': 'SR_Type_2'
}

# Read CSV and insert into MySQL in chunks
chunksize = 10000  # Adjust chunksize based on your system's memory
for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):
    chunk.rename(columns=column_mapping, inplace=True)
    chunk.to_sql(name='service_requests', con=engine, if_exists='append', index=False)
    print("Chunk inserted")

print("All data inserted")