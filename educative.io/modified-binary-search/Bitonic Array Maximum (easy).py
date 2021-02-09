def find_max_of_bitonic_array(arr):
    start, end = 0, len(arr)-1
    max_elem = -1
    while start <= end:
        middle = (start+end) // 2
        if middle+1 <= end and arr[middle] < arr[middle+1]:
            max_elem = max(max_elem, arr[middle+1])
            start = middle+1
        elif middle-1 >= start and arr[middle] < arr[middle-1]:
            max_elem = max(max_elem, arr[middle-1])
            end = middle-1
        else:
            max_elem = max(max_elem, arr[middle])
            return max_elem
    return max_elem

print(find_max_of_bitonic_array([1, 3, 8, 12, 4, 2])) #12
print(find_max_of_bitonic_array([3, 8, 3, 1])) #8
print(find_max_of_bitonic_array([1, 3, 8, 12])) #12
print(find_max_of_bitonic_array([10, 9, 8])) #10