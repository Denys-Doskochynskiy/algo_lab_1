from help_instrument import counters


def compare_element_from_heapsort(first_element, second_element):
    counters.compare_counter_heap += 1
    if first_element > second_element:

        return True
    else:

        return False


def heapify(zoos, n, i):
    largest = i
    l = 2 * i
    r = 2 * i + 1

    if l < n and compare_element_from_heapsort(zoos[i].visitors, zoos[l].visitors):
        largest = l

    if r < n and compare_element_from_heapsort(zoos[largest].visitors, zoos[r].visitors):
        largest = r

    if largest != i:
        zoos[i], zoos[largest] = zoos[largest], zoos[i]  # swap
        counters.swap_counter_heap += 1
        heapify(zoos, n, largest)



def heapSort(zoos):
    n = len(zoos)

    for i in range(n, -1, -1):
        heapify(zoos, n, i)


    for i in range(n - 1, 0, -1):
        zoos[i], zoos[0] = zoos[0], zoos[i]  # swap
        counters.swap_counter_heap += 1
        heapify(zoos, i, 0)
