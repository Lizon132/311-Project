# 311-Analysis: Urban Data Clustering and Correlation Analysis

## Overview

311-Analysis is a software suite designed to perform advanced spatial clustering and spatiotemporal correlation analysis of government 311 data. This tool aims to assist city planners and municipal decision-makers in understanding urban service request patterns and predicting future city service needs.

## Project Description

The 311-Analysis software comprises two main programs:

1. **Spatial Clustering Program**: This program employs a DBSCAN clustering algorithm to analyze 311 service request data spatially. It identifies clusters based on geographic proximity and calculates cluster centers. The data used includes various service request types like 'Air Pollution', 'Potholes', and 'Street Hazards', processed annually.

2. **Spatiotemporal Correlation Analysis Program**: Building upon the spatial clustering results, this program analyzes the temporal correlation between different service request types. It examines correlations within the same week and extends to subsequent weeks, thus unveiling patterns in service request occurrences over time.

## Technical Implementation

### Spatial Clustering
- Utilizes libraries like SQLAlchemy, Pandas, and scikit-learn.
- Connects to a MySQL database to fetch data.
- Processes and filters data for accurate clustering.
- Applies DBSCAN for spatial clustering.
- Saves clustering results in `cluster_centerpoints.csv`.

### Spatiotemporal Correlation Analysis
- Employs Geopandas and Shapely for spatial data manipulation.
- Imports clustered data from the first program.
- Implements the haversine formula for distance calculations.
- Analyzes correlations between different service request types.
- Generates a `correlation_results.csv` file with the analysis results.

## Applications

The 311-Analysis tool is tailored for city planners and public work managers, offering insights into the spatial distribution and temporal dynamics of urban service requests. By understanding these patterns, city officials can better predict and plan for future service needs, leading to more efficient use of municipal resources.

## Conclusion

311-Analysis provides a novel approach to urban service data analysis. Its combination of spatial clustering and spatiotemporal correlation analysis offers a comprehensive view of service request patterns, aiding in effective city planning and resource allocation.
