# Alteryx Workflow for Houston 311 Service Requests Analysis

## Overview

This Alteryx workflow processes and analyzes 311 service requests data from the City of Houston. It is designed to import data from the city's official website, apply necessary data transformations and filters, and then save the processed data to a local MySQL server, with each year's data stored in a separate but uniformly designed table.

## Data Source

The raw data for this workflow is sourced from the City of Houston's 311 service request portal, which can be accessed [here](https://www.houstontx.gov/311/). This data is comprehensive and includes various service request types submitted by the residents of Houston.

## Workflow Description

The workflow follows these main steps:

1. **Data Importing**: 
   - Imports data from the Houston 311 service request CSV files. The workflow is configured to handle files from different years, accommodating format changes that occurred mid-year in 2021.

2. **Data Processing and Filtering**:
   - Applies filters to clean and refine the data. This includes removing null values and selecting relevant fields based on specific criteria.
   - Regex functions are used to ensure data consistency, especially considering the format change in 2021.

3. **Data Exporting**:
   - Exports the processed data to a local MySQL server. Each year's data is saved in a distinct table, but all tables maintain a uniform structure for ease of use and consistency.

## Key Components

- **Tool Containers**: Organized into different sections for importing, processing, and exporting data.
- **Filter Tools**: Utilized to ensure data quality and relevance.
- **Database Tools**: Handle data interaction with the local MySQL server, ensuring each year's data is stored in separate, uniform tables.
- **Browse Tools**: Used for inspecting the data at various stages.

## Usage

To use this workflow:
1. Access the Houston 311 service request data from the provided URL and download the necessary CSV files.
2. Execute the workflow in Alteryx Designer, which will process and save the data to your local MySQL server, categorizing it by year.

## Requirements

- Alteryx Designer
- Access to the Houston 311 service requests data
- A local MySQL server setup

## Conclusion

This Alteryx workflow provides an efficient solution for handling, processing, and storing large datasets of 311 service requests from the City of Houston. Its ability to adapt to data format changes and store data in a structured manner makes it a valuable asset for data analysts and urban planners.
