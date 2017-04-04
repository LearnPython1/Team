import csv

fh_country = open("/Users/AMIT/python/country-list.csv", "r")
csv_file = csv.reader(fh_country)
#for line in csv_file:
    #print line
#fh_country.close()

dict = {}

list = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']

country_lines = fh_country.readlines()

for i in list:
 z=0
 for line in country_lines:
    y = line[1]
    if y == i:
     z = z + 1
    dict[i] = z
print dict