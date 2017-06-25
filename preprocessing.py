def import_data():
    input_file = open('/home/harsha/Downloads/LatLongData/IN.txt','r')
    country_list = []
    for line in input_file:
        point_list = []
        point = line.split("\t")
        point_list.append(point[2])
        point_list.append(point[4])
        point_list.append(point[5])
        country_list.append(point_list)
    return country_list