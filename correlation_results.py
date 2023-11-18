import pandas as pd
import numpy as np
from shapely.geometry import Point, shape
from geopandas import GeoDataFrame
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

def correlation_value(distance, max_distance_km):
    if distance <= max_distance_km:
        return 1 - (distance / max_distance_km)
    return 0

def main():
    try:
        sr_types = ['Air Pollution', 'Fire Hydrant', 'Flooding', 'Junk Motor Vehicle', 
                'Missed Garbage Pickup', 'Missed Heavy Trash Pickup', 
                'Missed Recycling Pickup', 'Parking Violation', 'Pothole', 
                'Street Condition', 'Street Hazard', 'Tree Removal']

        max_distance_km = 2.5

        # Import data from CSV
        df = pd.read_csv('cluster_centerpoints.csv')
        print("Data imported successfully.")

        df['geometry'] = df.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)
        gdf = GeoDataFrame(df, geometry='geometry')
        print("GeoDataFrame created.")

        result_rows = []

        for year in range(2011, 2024):
            print(f"Processing year: {year}")
            for week in range(1, 53):
                print(f"  Processing week: {week}")
                for sr_type1 in sr_types:
                    print(f"    Processing SR TYPE 1: {sr_type1}")
                    for offset in range(0, 4):
                        week2 = week + offset
                        if week2 > 52:
                            continue

                        for sr_type2 in sr_types:
                            if sr_type1 == sr_type2:
                                continue
                            print(f"      Comparing with SR TYPE 2: {sr_type2}, Offset: {offset}")

                            clusters1 = gdf[(gdf['Year'] == year) & (gdf['SR TYPE'] == sr_type1) & (gdf['Week'] == week)]
                            clusters2 = gdf[(gdf['Year'] == year) & (gdf['SR TYPE'] == sr_type2) & (gdf['Week'] == week2)]

                            for index, cluster1 in clusters1.iterrows():
                                max_correlation = 0
                                for _, cluster2 in clusters2.iterrows():
                                    distance = haversine(cluster1.geometry.x, cluster1.geometry.y, cluster2.geometry.x, cluster2.geometry.y)
                                    correlation = correlation_value(distance, max_distance_km)
                                    max_correlation = max(max_correlation, correlation)

                                result_rows.append({
                                    'Year': year,
                                    'Week': week,
                                    'SR TYPE 1': sr_type1,
                                    'ClusterID': cluster1['ClusterID'],
                                    'Latitude': cluster1['Latitude'],
                                    'Longitude': cluster1['Longitude'],
                                    'SR TYPE 2': sr_type2,
                                    'Offset': offset,
                                    'Correlation': max_correlation
                                })

        correlation_results = pd.DataFrame(result_rows)
        correlation_results.to_csv('correlation_results.csv', index=False)
        print("Correlation results saved to CSV.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print("Processing completed (whether successful or not).")

if __name__ == "__main__":
    main()