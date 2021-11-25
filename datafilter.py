import csv

rows = []

with open ("main.csv","r") as f :
    cr = csv.reader(f)
    for row in cr :
        rows.append(row)  
headers = rows[0]
print(headers)
headers[0] = "row_number"
print(headers)