def two_nums_hashmap(arr):
    hash_map ={}
    for i in arr:
        if i not in hash_map:
            hash_map[i] = 0
        else:
            del hash_map[i]
    return list(hash_map.keys())

# referred solution
def two_nums_xor(arr):
    xor_result = 0
    for i in range(len(arr)):
        xor_result ^= arr[i]
    # print(xor_result)
    right_most_one_bit_in_xor_result = 1
    while right_most_one_bit_in_xor_result & xor_result == 0:
        right_most_one_bit_in_xor_result <<= 1
    num1, num2 = 0, 0

    for i in arr:
        if right_most_one_bit_in_xor_result & i != 0:
            num1 ^= i
        else:
            num2 ^= i
    return [num1, num2]

# print("------Hashmap------")
# print(two_nums_hashmap([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])) #[4, 6]
# print(two_nums_hashmap([2, 1, 3, 2])) #[1, 3]
print("------XOR------")
print(two_nums_xor([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])) #[4, 6]
print(two_nums_xor([2, 1, 3, 2])) #[1, 3]