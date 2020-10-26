import csv
from help_instrument import counters
from my_array import MyArray


def read_price(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                numbers = MyArray([int(x) for x in row])
                return numbers


def read_discount(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row_discount in csv_reader:
            line_count += 1
        counters.discount_percent = float(row_discount[0])


def create_write_to_file(result):
    f = open("discount.csv", "w+")
    f.write(str(result))
    f.close()
