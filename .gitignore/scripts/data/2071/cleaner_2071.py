# Extracts name and gender field from 2071 data.

import csv
filename = 'ioe_2071.csv'

fp = open(filename)
reader = csv.DictReader(fp)

with open('ioe_20712_cleaned.csv', 'w') as wp:
    writer = csv.writer(wp)
    for line in reader:
        name = line['Student Name'].lower()
        gender = line['Gender'].lower()
        writer.writerow([name, gender])

fp.close()