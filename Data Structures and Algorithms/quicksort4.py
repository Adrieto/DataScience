def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, 0, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[j], arr[i] = arr[i], arr[j]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


array = [22, 11, 88, 66, 55, 77, 33, 44]


array = [22, 11, 88, 66, 55, 77, 125, 33, 15, 87, 47, 501, 44]

(quicksort(array, 0, len(array) - 1))

print(array)
