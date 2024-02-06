def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_number = 5

result = binary_search(array, target_number)

if result != -1:
    print(f"Искомый элемент {target_number} найден по индексу {result}.")
else:
    print(f"Искомый элемент {target_number} отсутствует в массиве.")
