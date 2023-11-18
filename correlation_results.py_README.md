# Urban Service Request Analysis Tool

## Overview

This Python application is designed to analyze urban service request data, focusing on spatial clustering and pattern recognition. The primary objective is to identify clusters of various service requests in urban areas and understand their distribution over time.

## Features

- **Spatial Clustering**: Utilizes the DBSCAN clustering algorithm to identify clusters of service requests based on geographical location.
- **Data Handling**: Employs Pandas and NumPy for efficient data manipulation and processing.
- **Database Integration**: Connects to a MySQL database to fetch relevant service request data.

## Clustering with DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is chosen for its proficiency in identifying clusters of arbitrary shape and its ability to handle noise in the dataset effectively. This algorithm is particularly well-suited for geographical data due to its flexibility in defining clusters based on density, allowing for the identification of high-concentration areas of service requests.

### Why DBSCAN?

- **Adaptability**: Capable of handling varied densities in urban service request data.
- **Noise Tolerance**: Effectively differentiates between core points, edge points, and outliers.
- **Parameter Configuration**: Uses `eps` (the maximum distance between two points for them to be considered as part of the same cluster) and `min_samples` (the minimum number of points to form a dense region), which are crucial in defining the granularity of the clustering.

## Geopandas Usage

Geopandas is used for its advanced capabilities in handling and analyzing spatial data. It extends the functionalities of Pandas, allowing for intuitive and efficient manipulation of geographical data, essential for analyzing and visualizing spatial patterns in urban service requests.

## Correlation Method

The application incorporates a method to analyze the correlation between different types of service requests. This approach is key to understanding how various urban issues are interconnected and how they evolve over time. The correlation analysis provides insights into the temporal dynamics of service requests, aiding in predictive modeling and resource allocation planning.

## Output

The result of the analysis is stored in `cluster_centerpoints.csv`, a file that contains the centroids of identified service request clusters along with relevant attributes like service request type, year, and week.

## Conclusion

This tool offers a comprehensive approach to analyzing urban service request data, providing city planners and public service providers with actionable insights into the spatial and temporal distribution of urban service requests.

