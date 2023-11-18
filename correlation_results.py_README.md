# Correlation Results Tool

## Overview

This Python application is designed to analyze urban service request data, focusing on spatial clustering and temporal correlations. It aims to provide city planners and municipal authorities with insights into service request patterns, aiding in efficient resource allocation and planning.

## Key Features

- **Spatial Clustering Analysis**: Identifies clusters of various urban service requests.
- **Temporal Correlation Analysis**: Examines the correlation between different service request types over time.
- **Data Export**: Outputs the results into a CSV file for further analysis or visualization.

## Technical Details

### Clustering Algorithm

The application uses DBSCAN (Density-Based Spatial Clustering of Applications with Noise), a widely recognized clustering algorithm known for its effectiveness in identifying clusters of arbitrary shapes and sizes in spatial data. This algorithm was chosen for its ability to handle noise in the dataset and its suitability for geographic data with varying densities.

### Geopandas Usage

Geopandas, an extension of Pandas, is utilized for its advanced capabilities in handling and analyzing spatial data. It allows the application to efficiently manage geographic data, perform spatial operations, and seamlessly integrate with other Python libraries used in the project.

### Correlation Method

The correlation method employed in the application is designed to measure the spatial and temporal proximity between different types of service requests. This approach provides a nuanced understanding of how various urban issues are interconnected, enabling more informed decision-making by city authorities.

### Haversine Formula

The Haversine formula is implemented to calculate the great-circle distances between points, which is essential for accurate distance measurement on the Earth's surface. This formula is critical in determining the proximity of different service requests, forming the basis of the correlation analysis.

## How to Use

1. Run the application to process the data from `cluster_centerpoints.csv`.
2. The application will analyze spatial and temporal correlations between service request types.
3. Upon completion, the results will be saved in `correlation_results.csv`.

## Requirements

- Python 3.x
- Libraries: Pandas, NumPy, Shapely, Geopandas

## Conclusion

This tool offers a comprehensive approach to analyzing urban service requests, combining spatial clustering with temporal correlation analysis. Its insights can guide city planners in proactive decision-making and effective urban management.
