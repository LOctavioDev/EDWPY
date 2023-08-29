import csv

#LEER UN ARCHIVO CSV
with open('C:/Users/52771/Documents/EDWPY/CSV/csv_example.csv', 'r') as filecsv:
    reader = csv.reader(filecsv)
    for row in reader:
        print(', '.join(row))

#ESCRIBIR UN ARVICHO CSV
with open('C:/Users/52771/Documents/EDWPY/CSV/csv_example.csv', 'a') as filecsva:
    writer = csv.writer(filecsva)
    writer.writerow(['Marco','Ramirez','26529828','marcogod@gmail.com'])
