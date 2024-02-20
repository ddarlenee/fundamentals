# csv file (variable length)
import csv

# Read
with open('data.csv', 'r') as file:
    # create reader object
    reader = csv.reader(file) 
    # prints the info about the reader
    print(reader)

# Write
data = [
    ['field1', 'field2'],  # Example: Header row
    ['value1', 'value2'],  # Example: Data row 1
    ['value3', 'value4']   # Example: Data row 2
]
# ensures that no additional line endings are added
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
