import csv

database_csv_file = {}
with open("database.csv", "r") as file:
    file_read = csv.reader(file, delimiter=',')
    database_csv_file = {row[0]: row[0] for row in file}


print(database_csv_file)
#print(database_csv_file.index([*'John'*]))
