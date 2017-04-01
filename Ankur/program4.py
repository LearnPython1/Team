import csv
#
# x = open('C:\Users\Ankur\Desktop\country_list.txt', "r")
# for line in x:
#     line = line.rstrip()
#     if line.find(' the ') == -1 :
#         continue
#     print line

fh_country = open('C:\Users\Ankur\Desktop\country_list.txt', "r")
country_lines = fh_country.readlines()
counntry_names = []
capitals = []
#x = country_lines[]

for line in country_lines[1:]:
    country = line.strip().split(',')[0]
    capital = line.strip().split(',')[1]
    #counntry_names.append(a)
    #if 'Sri' in country and 'Sri' in capital:
    if country == capital:
        capitals.append(country)

print capitals
fh_country.close()


