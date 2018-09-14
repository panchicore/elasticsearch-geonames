import csv

admin1 = []
admin2 = []

with open('admin1CodesASCII.txt', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        admin1.append(row)


print "generating dict_admin1_geonameid.csv..."

with open('dict_admin1_geonameid.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in admin1:
        spamwriter.writerow([row[3], "1"])


print "generating dict_admin1_feature.csv..."

with open('dict_admin1_feature.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in admin1:
        spamwriter.writerow([row[0], "{}__{}".format(row[2], row[1])])


with open('admin2Codes.txt', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        admin2.append(row)


print "generating dict_admin2_geonameid.csv..."

with open('dict_admin2_geonameid.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in admin2:
        spamwriter.writerow([row[3], "1"])

with open('dict_admin2_feature.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in admin2:
        spamwriter.writerow([row[0], "{}__{}".format(row[2], row[1])])



print "OK"