import csv
import sys

file_handler = open(sys.argv[1], 'rt')
try:
    reader = csv.DictReader(file_handler)
    for row in reader:
        print(row['Title 1'] + ' sd')
finally:
    file_handler.close()
