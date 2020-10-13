from help_instrument import counters
from sort_algorithm.heap_sort import heapSort
from sort_algorithm.insertion_sort import insertionSort
from help_instrument.csv_reader import read_file_csv
import time
if __name__ == '__main__':

    file = input("Enter please filename:")
    zoos = read_file_csv(file)

    n = len(zoos)
    heap_time_start = time.time()
    heapSort(zoos)
    heap_time = time.time() - heap_time_start
    heap_time_in_ms=heap_time*10000
    print("Sorted zoo using heapsort")
    for i in range(n):
        print(zoos[i])

    insertion_time_start = time.time()
    insertionSort(zoos)
    insertion_time = time.time() - insertion_time_start
    insertion_time_in_ms=insertion_time*10000
    print("Sorted zoo using insertsort")
    for i in range(n):
        print(zoos[i])
    print("#####################################")
    print("amount swap in insertsort")
    print(counters.swap_counter_insert)
    print("amount compare in insertsort")
    print(counters.compare_counter_insert)
    print("Time for sorting: "+str(insertion_time_in_ms))
    print("#####################################")
    print("amount of swap in heapsort")
    print(counters.swap_counter_heap)
    print("amount compare in heapsort")
    print(counters.compare_counter_heap)
    print("Time for sorting: " + str(heap_time_in_ms))
    print("#####################################")


