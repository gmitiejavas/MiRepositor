import csv
csv_example = open("CSV-Example.csv")
csv_python = csv.reader(csv_example)
print(type(csv_python))
print(csv_python)

for row in csv_python:
    print("{} esta en  {} y tiene la direccion {}".format(row[0], row[2], row[1]))
