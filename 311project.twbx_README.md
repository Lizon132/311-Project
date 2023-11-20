# 311 Project Dashboard

## Overview

The 311 Project Dashboard is an interactive visualization tool developed by Christopher Aguirre for the Fall of 2023. This dashboard provides insights into various service request types (SR TYPE) reported in the city, offering a comprehensive analysis of the patterns and correlations between different types of service requests over time.

## Features

- **Parameter Selection**: Users can filter data by selecting specific SR TYPES, year, and week of interest from dropdown menus.
- **General Map**: A map view that shows the distribution of service requests across the city for the selected parameters.
- **Cluster Map**: This map displays clusters of service requests to identify high-density areas.
- **Correlation Map**: Visual representation of the correlation between two selected SR TYPES, with the ability to observe the impact of one service request type on another over a period of 0-3 weeks.

## Data Sources

The dashboard utilizes a dataset encompassing approximately 200k data points across 12 different SR TYPES and 11 different time references spanning from 2011 to 2023.

## Interactive Elements

- **Parameters 1 & 2**: Two drop-down selectors that allow the user to choose which SR TYPES to compare.
- **Week Offset Slider**: An interactive slider that sets the number of weeks between the occurrences of the first and second SR TYPES.
- **Year and Week Selector**: Drop-down menus for selecting the specific year and week for the analysis.

## Visualization Details

- **SR TYPE Color Coding**: Each SR TYPE is color-coded for easy identification, with a consistent color palette used across different maps for coherence.
- **Dynamic Title**: The dashboard title includes the year and week selected by the user and updates dynamically based on user interaction.

## Usage

The dashboard is designed to be user-friendly, allowing city planners, public workers, and citizens to interact with the data seamlessly. Users can identify patterns, such as an increase in potholes following flooding events, and make informed decisions based on the visualized data.

## Technical Details

The dashboard is built using Tableau and incorporates advanced calculations to filter data dynamically based on user input. It leverages geographic clustering algorithms to group data points and compute correlations within a specified radius.

## Disclaimer

This dashboard is for educational purposes and demonstrates the capabilities of data visualization in understanding urban issues.

## Feedback

For suggestions or issues, please contact [Christopher Aguirre's GitHub](https://github.com/christopheraguirre).

---

**Note**: The GitHub link is a placeholder and should be replaced with the actual URL to the project repository on GitHub.
