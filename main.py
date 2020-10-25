from help_instrument import counters
from sort_algorithm.heap_sort import heapSort

from help_instrument.csv_reader import read_file_csv
import time

if __name__ == '__main__':

    file = input("Enter please filename:")
    zoos = read_file_csv(file)

    n = len(zoos)
    count_max_element = int(n / 3)
    print(count_max_element)
    heap_time_start = time.time()
    heapSort(zoos,count_max_element)
    heap_time = time.time() - heap_time_start
    heap_time_in_ms = heap_time * 10000
    print("Sorted zoo using heapsort")
    for i in range(n):
        print(zoos[i])
        counters.total_price += zoos[i].price

    print("#####################################")

    print("amount of swap in heapsort")
    print(counters.swap_counter_heap)
    print("amount compare in heapsort")
    print(counters.compare_counter_heap)
    print("Time for sorting: " + str(heap_time_in_ms))
    print("Total price discount " + str(counters.discount * 0.1))
    print("Total price  " + str(counters.total_price))
    print("Total price with discount " + str(counters.total_price - (counters.discount * 0.1)))
    print("#####################################")
