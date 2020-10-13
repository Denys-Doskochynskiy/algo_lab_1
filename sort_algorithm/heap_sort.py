from help_instrument import counters


def compare_element_from_heapsort(first_element, second_element):
    counters.compare_counter_heap += 1
    if first_element > second_element:

        return True
    else:

        return False


def heapify(zoos, zoo_length, index):
    largest_index = index
    child_left = 2 * index + 1
    child_right = 2 * index + 2

    if child_left < zoo_length and compare_element_from_heapsort(zoos[index].visitors, zoos[child_left].visitors):
        largest_index = child_left

    if child_right < zoo_length and compare_element_from_heapsort(zoos[largest_index].visitors,
                                                                  zoos[child_right].visitors):
        largest_index = child_right

    if largest_index != index:
        zoos[index], zoos[largest_index] = zoos[largest_index], zoos[index]  # swap
        counters.swap_counter_heap += 1
        heapify(zoos, zoo_length, largest_index)


def heapSort(zoos):
    zoo_length = len(zoos)

    for i in range(zoo_length, -1, -1):
        heapify(zoos, zoo_length, i)

    for i in range(zoo_length - 1, 0, -1):
        zoos[i], zoos[0] = zoos[0], zoos[i]  # swap
        counters.swap_counter_heap += 1
        heapify(zoos, i, 0)
