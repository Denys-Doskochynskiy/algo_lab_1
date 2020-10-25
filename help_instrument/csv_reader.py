import csv
from zoo import Zoo


def read_file_csv(file_name):
    list_of_zoos = []
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            list_of_zoos.append(Zoo(int(row[0]), int(row[1])))
        return list_of_zoos
