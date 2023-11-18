# 311 Service Requests Data Importer

## Overview

This Python application is designed to import large datasets of urban service requests into a MySQL database efficiently. It is particularly useful for managing extensive data from 311 service requests, enabling easy storage and access for further analysis.

## Key Features

- **Efficient Data Import**: Imports data from a CSV file into a MySQL database using chunks for memory efficiency.
- **Column Mapping**: Maps CSV headers to MySQL table column names, ensuring data consistency.
- **Chunk-wise Processing**: Processes the CSV file in manageable chunks, optimizing memory usage and performance.

## Technical Details

### Database Connection

The application uses SQLAlchemy to establish a connection with a MySQL database. The engine is configured to connect to the `project_311` database on the localhost.

### CSV File Handling

The application reads data from a specified CSV file path, which contains the exported results of 311 service requests correlation analysis.

### Column Name Mapping

To maintain consistency between the CSV file headers and the MySQL table column names, a column mapping dictionary is used. This dictionary defines how the CSV headers ('SR TYPE 1', 'SR TYPE 2') are mapped to the respective database column names ('SR_Type_1', 'SR_Type_2').

### Chunk-wise Data Insertion

Data from the CSV file is read and inserted into the database in chunks, with each chunk size set to 10,000 rows. This approach ensures that the data import process is memory efficient, particularly important for large datasets.

## How to Use

1. Ensure the MySQL database and table (`service_requests`) are set up.
2. Update the `csv_file_path` in the script to point to your CSV file.
3. Run the script to start importing data into the database.
4. The script will output a message for each chunk inserted and a final confirmation once all data is imported.

## Requirements

- Python 3.x
- Libraries: Pandas, SQLAlchemy
- MySQL database access

## Conclusion

This tool streamlines the process of importing large sets of 311 service requests data into a MySQL database, facilitating efficient data management and analysis for urban planners and data analysts.
