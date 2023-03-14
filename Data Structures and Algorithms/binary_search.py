"""You're going to write a binary search function.
You should use an iterative approach - meaning using loops.
Your function should take two inputs:
a Python list to search through, and the value you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

# ================================================
# EJERCICIO APROBADO
# ================================================


def binary_search(input_array, value):
    index = None
    aux_idx = 0
    while index == None:
        if len(input_array) >= 2:
            cut_point = (
                (int(len(input_array) / 2))
                if (len(input_array) % 2 == 0)
                else int(len(input_array) / 2 + 1)
            )

            left = input_array[:cut_point]
            right = input_array[cut_point:]

            for idx, element in enumerate(left):

                if element == value:
                    index = aux_idx + idx
                    break

            input_array = right
            aux_idx += len(left)

        elif len(input_array) == 1 and value == input_array[0]:
            index = 0
        else:
            index = -1

    return index


test_list = [1, 3, 9, 11, 15, 19, 29]
test_list2 = [1, 3]
test_list3 = [1]
test_val1 = 25
test_val2 = 15
test_val3 = 1
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list2, test_val2))
print(binary_search(test_list3, test_val3))
