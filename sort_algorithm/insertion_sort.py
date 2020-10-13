from help_instrument import counters


def insertionSort(zoos):
    for index_zoo in range(1, len(zoos)):

        key_atribute = zoos[index_zoo].how_many_animals
        key = zoos[index_zoo]
        zoos_from_insert = index_zoo - 1
        while zoos_from_insert >= 0 and compare_element_from_insertsort(key_atribute,
                                                                        zoos[zoos_from_insert].how_many_animals):
            zoos[zoos_from_insert + 1] = zoos[zoos_from_insert]
            zoos_from_insert -= 1
            counters.swap_counter_insert += 1
        zoos[zoos_from_insert + 1] = key
        counters.swap_counter_insert += 1


def compare_element_from_insertsort(first_element, second_element):
    counters.compare_counter_insert += 1
    if first_element < second_element:

        return True
    else:

        return False
