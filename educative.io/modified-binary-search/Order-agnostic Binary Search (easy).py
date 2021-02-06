def modified_binary_search(arr, key):
    is_ascending, is_descending = False, False
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            is_ascending = True
        elif arr[i] > arr[i+1]:
            is_descending = True
    start, end = 0, len(arr)-1
    middle = (start + end) // 2
    while start <= end:
        if arr[middle] == key:
            return middle
        elif is_ascending and arr[middle] > key:
            end = middle - 1
            middle = (start + end) // 2
        elif is_ascending and arr[middle] < key:
            start = middle+1
            middle = (start + end) // 2
        elif is_descending and arr[middle] < key:
                end = middle - 1
                middle = (start + end) // 2
        elif is_descending and arr[middle] > key:
            start = middle+1
            middle = (start + end) // 2
    # Longer way of the above code
    # if is_ascending:
    #     while start <= end:
    #         if arr[middle] == key:
    #             return middle
    #         elif arr[middle] > key:
    #             end = middle - 1
    #             middle = (start + end) // 2
    #         elif arr[middle] < key:
    #             start = middle+1
    #             middle = (start + end) // 2
    # else:
    #     while start <= end:
    #         if arr[middle] == key:
    #             return middle
    #         elif arr[middle] < key:
    #             end = middle - 1
    #             middle = (start + end) // 2
    #         elif arr[middle] > key:
    #             start = middle+1
    #             middle = (start + end) // 2
    return -1

print(modified_binary_search([4, 6, 10], 10))
print(modified_binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(modified_binary_search([10, 6, 4], 10))