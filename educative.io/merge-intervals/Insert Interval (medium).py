def newLogic(nums):
    print(nums)
    start = nums[0][0]
    end = nums[0][1]
    result = []
    for i in range(1, len(nums)):
        if nums[i][0] <= end:
            end = max(nums[i][1], end)
        else:
            result.append([start, end])
            start = nums[i][0]
            end = nums[i][1]
    result.append([start, end])
    return result

def insertInterval(nums, newInterval):
    merged = []
    i = 0
    while nums[i][1] < newInterval[0]:
        merged.append(nums[i])
        i += 1
    merged.append(newInterval)
    while i < len(nums):
        merged.append(nums[i])
        i += 1
    return merged

def main():
    nums = [[1,3], [5,7], [8,12]]
    newInterval = [4,6]
    nums = insertInterval(nums, newInterval)
    print(newLogic(nums))

main()