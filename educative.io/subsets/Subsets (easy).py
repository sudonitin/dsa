# Since, in each step, the number of subsets doubles
# as we add each element to all the existing subsets,
# the time complexity of the above algorithm is O(2^N)
# ​​where ‘N’ is the total number of elements in the input set.
# This also means that, in the end, we will have a total of O(2^N)
# ​​subsets.

# time and space complexity both are 2^N

def find_all_subsets(arr):
    result = [[]]
    for i in arr:
        temp = []
        result_len = len(result)
        for subset in range(result_len):
            # print(result[subset] + [i])
            temp.append(result[subset] + [i])
        result += temp
    return result

# print(find_all_subsets([1,3]))
# print(find_all_subsets([1,5,3]))
print(find_all_subsets(["B", "A", "T"]))