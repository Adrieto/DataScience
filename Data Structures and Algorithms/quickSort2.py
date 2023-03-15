import time


def quicksort(array):
    right_to_left = len(array) - 1  # Position in the array starting on the right
    left_to_right = 0  # Position in the array starting on the left
    pivot = array[-1]
    print(array, left_to_right, right_to_left)
    # pivot_displacement = 0  # The first pivot is the last element

    while True:  ###
        # while right_to_left - left_to_right > 1:
        while pivot < array[left_to_right]:
            array[right_to_left] = array[0 + left_to_right]
            array[0 + left_to_right] = array[right_to_left - 1]
            array[right_to_left - 1] = pivot

            right_to_left -= 1
            print(array, left_to_right, right_to_left, pivot, array[left_to_right])

        if right_to_left - left_to_right == 0:  ### Same position

            break  ###

        else:  ###
            left_to_right += 1  ###

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
(quicksort(test))


# La version que andaba hasta el momento:
"""def quicksort(array):
    right_to_left = len(array) - 1  # Position in the array starting on the right
    left_to_right = 0  # Position in the array starting on the left
    pivot = array[-1]
    print (array, left_to_right, right_to_left)
    #pivot_displacement = 0  # The first pivot is the last element

    while right_to_left - left_to_right > 1: 
        while pivot < array[left_to_right]: 
            array[right_to_left] = array[0 + left_to_right]
            array[0 + left_to_right] = array[right_to_left - 1]
            array[right_to_left - 1] = pivot   


            right_to_left -= 1
            print (array, left_to_right, right_to_left, pivot, array[left_to_right] )
        
        left_to_right += 1
        
        
    return array"""
