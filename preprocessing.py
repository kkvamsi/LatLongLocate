def import_data():
    count = 0
    input_file = open('/home/harsha/Downloads/LatLongData/IN.txt','r')
    country_list = []
    for line in input_file:
        count = count + 1
        point_list = []
        point = line.split("\t")
        point_list.append(point[2])
        point_list.append(point[4])
        point_list.append(point[5])
        if count < 10 :
            print point_list
    print count

import_data()