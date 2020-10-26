from help_instrument import counters
from sort_algorithm.heap_sort import heapSort
from help_instrument.csv_reader import read_discount
from help_instrument.csv_reader import read_price
from help_instrument.csv_reader import create_write_to_file
from my_array import MyArray

if __name__ == '__main__':

    file = input("Enter please filename:")
    zoos = read_price(file)
    read_discount(file)

    if counters.discount_percent > 1:
        counters.discount_percent = 0
        if counters.discount_percent < 0:
            counters.discount_percent = 0
    n = len(zoos)
    if n < 10000:
        count_max_element = int(n / 3)
        heapSort(zoos, count_max_element)
        for i in range(n):
            counters.total_price += int(zoos[i])
        print(counters.total_price)
    else:
        count_max_element = 0
        counters.total_price = 0

    print("#####################################")

    price_discount = counters.discount * counters.discount_percent
    print("Total price discount " + str(price_discount))
    print("Total price  " + str(counters.total_price))
    total_price_with_discount = round(counters.total_price - price_discount, 2)

    print("Total price with discount " + str(total_price_with_discount))
    print("#####################################")
    create_write_to_file(total_price_with_discount)
    print("Your file is ready!)))")
    print("#####################################")
