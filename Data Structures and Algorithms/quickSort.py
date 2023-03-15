"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
import time


def quicksort(array):

    pivot = array[-1]
    pivot_displacement = 0  # The first pivot is the last element

    for i in range(len(array) - pivot_displacement):

        while pivot < array[i]:
            pivot_position = (len(array) - 1) - pivot_displacement

            if abs(pivot_position - i) > 1:

                array[pivot_position] = array[i]  # Position where pivot was
                array[i] = array[
                    pivot_position - 1
                ]  # replaced with the value on the left of pivot
                array[pivot_position - 1] = pivot  # pivot is moved to the left

                print(array, pivot_displacement, pivot_position, i, pivot)
                pivot_displacement += 1

            elif abs(pivot_position - i) == 1:
                array[pivot_position] = array[i]
                array[i] = pivot

                pivot_displacement += 1
                print(array, pivot_displacement, pivot_position, i, pivot, "ACA")

            """else:
                pivot = array[i-2] if i>=1 else array[0]
                i = 0
                
                print(array, pivot_displacement, pivot_position, i, pivot, array[i], "en else")
                time.sleep(2)"""

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
