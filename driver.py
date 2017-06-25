import distance
import preprocessing
import sys
import time

def calculate_distance(lat, long):
    country_list = preprocessing.import_data()
    nearest_distance = sys.maxint
    nearest_point = ""
    for point in country_list:
        point_distance = distance.haversine(float(long), float(lat), float(point[2]), float(point[1]))
        if nearest_distance > point_distance:
            nearest_distance = point_distance
            nearest_point = point[0]
    print nearest_point

start_time = time.time()
calculate_distance(17.38405, 78.45636)
end_time = time.time()
print end_time - start_time