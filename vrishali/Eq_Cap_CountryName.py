import csv

fh_country = open("/Users/AMIT/python/country-list.csv", "r")
#csv_file = csv.reader(fh_country)
#for line in csv_file:
    #print line
#fh_country.close()

list = []
country_lines = fh_country.readlines()
for line in country_lines:
 x=line
 y = x[1]
 y = x.strip().split(',')[1]
 z = x.strip().split(',')[0]
 if y == z:
  list.append(y)
print "Equal Country name and Capital: ", list
