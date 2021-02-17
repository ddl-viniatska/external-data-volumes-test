import csv

with open('/domino/edv/smb_diabetes_read_only/diabetes.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
