# Urban Service Request Analysis Tool

## Overview

This Python application is designed to analyze urban service request data, leveraging advanced spatial clustering techniques. By processing government 311 data, the tool aims to provide city planners and municipal authorities with insights into the distribution and frequency of various urban service requests.

## Key Features

- **Spatial Clustering**: Utilizes the DBSCAN clustering algorithm to identify clusters of service requests.
- **Data Filtering**: Filters and processes data for accurate analysis.
- **Customizable Parameters**: Allows setting parameters like the desired distance for clustering.
- **Extensive Data Handling**: Handles multiple types of service requests over several years.

## Clustering Algorithm: DBSCAN

The choice of the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm is pivotal to the application's functionality. DBSCAN is selected for its ability to form clusters of arbitrary shape and handle outliers effectively, which is essential in the varied and noisy urban data environment. The algorithm uses a specified radius (`eps`) to determine the neighborhoods around each point and requires a minimum number of points (`min_samples`) to form a cluster, making it adaptable to different data densities.

### Why DBSCAN?

- **Flexibility in Cluster Formation**: Unlike algorithms that assume spherical clusters, DBSCAN can form clusters of any shape, which is more realistic for urban data.
- **Noise Handling**: DBSCAN effectively identifies and separates outliers, ensuring cleaner and more meaningful clustering results.
- **No Need to Specify Cluster Number**: DBSCAN does not require the number of clusters to be defined a priori, making it ideal for datasets where the number of clusters is unknown.

## Implementation Details

- **Database Connection**: Utilizes SQLAlchemy to connect to a MySQL database and fetch service request data.
- **Data Processing**: Employs Pandas and NumPy for data manipulation and filtering.
- **Haversine Distance Calculation**: Converts latitudes and longitudes to radians and calculates distances using the haversine formula, considering the Earth's curvature.
- **Results Storage**: Aggregates and stores clustering results in a DataFrame, which is then exported to a CSV file (`cluster_centerpoints.csv`).

## Usage

This tool is designed for use by city administrators, urban planners, and researchers interested in urban dynamics. By analyzing spatial patterns in service requests, the tool aids in efficient resource allocation, urban planning, and identifying areas requiring attention.

## Output

- **File Generated**: `cluster_centerpoints.csv`
- **Contents**: Cluster identifiers, year, week, service request type, and geographical coordinates of cluster centers.

## Conclusion

This Python application stands as a sophisticated tool for urban data analysis, offering a window into the spatial dimensions of city service needs. Its utilization of DBSCAN for spatial clustering represents an innovative approach in urban analytics.
