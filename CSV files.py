import csv

with open('cars.csv', 'r') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for row in rows:
        print(row)

new_cars = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault',  'Clio', 2008, 90]
]

with open('cars.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for new_row in new_cars:
        csv_writer.writerow(new_row)

with open('cars.csv', 'r', newline='') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for row in rows:

        print(row)