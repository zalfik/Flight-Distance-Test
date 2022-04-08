import numpy as np
import pandas as pd
from numpy import pi, radians, arccos, sin, cos


# Calculate distance (in miles) of two points with Haversine formula (with Spherical Law of Cosines)
def distance(d_lat, d_lon, a_lat, a_lon):
    d_lat, d_lon, a_lat, a_lon = map(radians, [d_lat, d_lon, a_lat, a_lon])
    radious = 3958.8 # Earth radious in miles  
    calculate_distance = round(arccos(sin(d_lat) * sin(a_lat) + cos(d_lat) * cos(a_lat) * cos(a_lon - d_lon))*radious)
    return(calculate_distance)


filename = 'Flight_Distance_test.csv'
df = pd.read_csv(filename)
df["Distance"] = distance(df["Departure_lat"],df["Departure_lon"], df["Arrival_lat"], df["Arrival_lon"])
df = df.astype({"Distance": int})

print(df)