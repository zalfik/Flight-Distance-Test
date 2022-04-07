import pandas as pd
from math import pi, radians, acos, sin, cos


# Calculate distance (in miles) of two points with Haversine formula (with Spherical Law of Cosines)
def distance(d_lat, d_lon, a_lat, a_lon):
    d_lat, d_lon, a_lat, a_lon = map(radians, [d_lat, d_lon, a_lat, a_lon])
    radious = 3958.8 # Earth radious in miles  
    calculate_distance = round(acos(sin(d_lat) * sin(a_lat) + cos(d_lat) * cos(a_lat) * cos(a_lon - d_lon))*radious)
    return(calculate_distance)

print(distance(1.3,103.98,51.47,-0.45))  # test


df = pd.read_csv('Flight_Distance_test.csv')

print(df.columns)