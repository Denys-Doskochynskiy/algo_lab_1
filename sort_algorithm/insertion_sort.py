from help_instrument import counters


def insertionSort(zoos):

    for i in range(1, len(zoos)):

        key_atribute = zoos[i].how_many_animals
        key = zoos[i]
        j = i - 1
        while j >= 0 and compare_element_from_insertsort(key_atribute, zoos[j].how_many_animals):
            zoos[j + 1] = zoos[j]
            j -= 1
            counters.swap_counter_insert += 1
        zoos[j + 1] = key
        counters.swap_counter_insert += 1




def compare_element_from_insertsort(first_element, second_element):
    counters.compare_counter_insert += 1
    if first_element < second_element:

        return True
    else:

        return False

