import time


def quicksort(array):
    right_to_left = len(array) - 1  # Position in the array starting on the right
    left_to_right = 0  # Position in the array starting on the left
    pivot = array[-1]
    print(array, left_to_right, right_to_left)
    # pivot_displacement = 0  # The first pivot is the last element

    while True:  ###

        if right_to_left - left_to_right > 1:  ### Same position
            array, pivot, left_to_right, right_to_left = loop(
                array, pivot, left_to_right, right_to_left
            )
            print(
                array,
                left_to_right,
                right_to_left,
                pivot,
                array[left_to_right],
                pivot < array[left_to_right],
            )

        elif right_to_left - left_to_right == 0:  ### Same position
            break_point = right_to_left

            print("entra elif")

            break  ###

        else:  ###

            print(f"ENTRO ELSEEEE. L_to_R = {left_to_right}")
        # print("no termino mas")
        time.sleep(0.4)
    return array


def loop(array, pivot, left_to_right, right_to_left):
    while right_to_left - left_to_right > 1:
        while pivot < array[left_to_right]:
            array[right_to_left] = array[0 + left_to_right]
            array[0 + left_to_right] = array[right_to_left - 1]
            array[right_to_left - 1] = pivot

            print(
                f"En la funcion: {array}, {left_to_right}, {right_to_left}, {pivot}, {array[left_to_right]}, {pivot < array[left_to_right]}"
            )
            right_to_left -= 1
            if right_to_left == left_to_right:
                return array, pivot, left_to_right, right_to_left

        left_to_right += 1


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
(quicksort(test))
