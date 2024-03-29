
def find_all_unique_subsets(arr):
    arr.sort()
    result = [[]]
    duplicateCount = 0
    for i in range(len(arr)):
        temp = []
        if i != 0:
            if arr[i-1] != arr[i]:
                duplicateCount = 0
                result_len = len(result)
                for subset in range(result_len):
                    temp.append(result[subset] + [arr[i]])
                result += temp
            else:
                duplicateCount += 1
                # skip first 2^duplicateCount
                result_len = len(result)
                for subset in range(result_len):
                    if subset > 2**duplicateCount-1:
                        temp.append(result[subset] + [arr[i]])
                result += temp
        else:
            result_len = len(result)
            for subset in range(result_len):
                temp.append(result[subset] + [arr[i]])
            result += temp
    return result

# almost same logic optimised the duplicateCount part 
# by maintaining startIndex and endIndex
def referredLogic(arr):
    arr.sort()
    result = [[]]
    startIndex, endIndex = 0, 0
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            startIndex = endIndex + 1
        endIndex = len(result)
        if i > 0 and arr[i] == arr[i-1]:
            print(startIndex, endIndex)
        for j in range(startIndex, endIndex):
            temp = list(result[j])
            temp.append(arr[i])
            result.append(temp)
    return result

# print(find_all_subsets([1,3]))
# print(find_all_unique_subsets([1,3,3]))
# print(find_all_unique_subsets([1, 5, 3, 3]))
print(referredLogic([1,3,3]))