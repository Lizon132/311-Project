from sqlalchemy import create_engine
import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
from math import radians

# Function to convert lat/long to radians for haversine distance
def latlong_to_radians(lat, long):
    return [radians(lat), radians(long)]

# Create an SQLAlchemy engine for the database connection
engine = create_engine('mysql+mysqlconnector://root:Firepower#132@localhost/project_311')

# List of SR TYPES to process
sr_types = ['Air Pollution', 'Fire Hydrant', 'Flooding', 'Junk Motor Vehicle', 
            'Missed Garbage Pickup', 'Missed Heavy Trash Pickup', 
            'Missed Recycling Pickup', 'Parking Violation', 'Pothole', 
            'Street Condition', 'Street Hazard', 'Tree Removal']

# Earth's radius in kilometers for haversine calculation
earth_radius_km = 6371.0088

# Desired distance in kilometers for DBSCAN
desired_distance_km = 0.25  # For example, 1 kilometer

# Initialize DataFrame to store all results
all_clusters = pd.DataFrame(columns=['ClusterID', 'Year', 'Week', 'SR TYPE', 'Latitude', 'Longitude'])

# Initialize cluster ID counter
cluster_id_counter = 1

for year in range(2011, 2024):
    table_name = f"year{year}"
    for sr_type in sr_types:
        # Query with case-insensitive column names and handling different date formats
        query = f"""
        SELECT 
            IFNULL(LATITUDE, `Latitude`) AS Latitude, 
            IFNULL(LONGITUDE, `Longitude`) AS Longitude, 
            WEEK(CASE 
                WHEN `SR CREATE DATE` LIKE '%%/%%/20%% %%:%%' THEN STR_TO_DATE(`SR CREATE DATE`, '%c/%e/%Y %H:%i')
                ELSE STR_TO_DATE(`SR CREATE DATE`, '%c/%e/%Y') 
            END) AS Week
        FROM {table_name}
        WHERE `SR TYPE` = '{sr_type}' AND YEAR(CASE 
                WHEN `SR CREATE DATE` LIKE '%%/%%/20%% %%:%%' THEN STR_TO_DATE(`SR CREATE DATE`, '%c/%e/%Y %H:%i')
                ELSE STR_TO_DATE(`SR CREATE DATE`, '%c/%e/%Y') 
            END) = {year}
        """
        data = pd.read_sql(query, engine)

        # Filter out rows where Latitude or Longitude are 0.0
        data = data[(data['Latitude'] != 0.0) & (data['Longitude'] != 0.0)]
        
        # Drop rows with NaN values in 'Latitude' or 'Longitude'
        data = data.dropna(subset=['Latitude', 'Longitude'])

        if data.empty:
            continue

        # Convert latitude and longitude to radians
        data_rad = np.array(data[['Latitude', 'Longitude']].apply(lambda row: latlong_to_radians(*row), axis=1).tolist())

        # Use DBSCAN for clustering
        db = DBSCAN(eps=desired_distance_km / earth_radius_km, min_samples=1, algorithm='ball_tree', metric='haversine')
        db.fit(data_rad)
        data['Cluster'] = db.labels_

        # Extract cluster centers and remove clusters centered at 0.0, 0.0
        cluster_centers = data.groupby('Cluster').mean()
        cluster_centers = cluster_centers[(cluster_centers['Latitude'] != 0.0) & (cluster_centers['Longitude'] != 0.0)]

        # Assign ClusterID and add Year, Week, and SR TYPE info
        cluster_centers['ClusterID'] = range(cluster_id_counter, cluster_id_counter + len(cluster_centers))
        cluster_id_counter += len(cluster_centers)
        cluster_centers['Year'] = year
        cluster_centers['SR TYPE'] = sr_type
        cluster_centers['Week'] = data.groupby('Cluster')['Week'].first()

        # Append to the results DataFrame
        all_clusters = pd.concat([all_clusters, cluster_centers.reset_index()[['ClusterID', 'Year', 'Week', 'SR TYPE', 'Latitude', 'Longitude']]], ignore_index=True)

# Save results to CSV
all_clusters.to_csv('cluster_centerpoints.csv', index=False)