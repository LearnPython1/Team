print "Hello World"

print "my first code change"

import csv

fh_country = open("/Users/Amit/python/country-list.csv", "r")
csv_file = csv.reader(fh_country)

for line in csv_file:
    print line

fh_country.close()
