# same bug (solution from educative)
def newLogic(nums):
    nums.sort(key=lambda x:x[0])
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

# a bit buggy
def mergeIntervals(nums):
    # sort the intervals in ascending order based on start
    nums.sort(key=lambda x:x[0])
    print(nums)
    i = 1
    result = []
    # c = []
    while i < len(nums):
        if nums[i][0] <= nums[i-1][1]: # if b.start <= a.end (i.e. a overlaps b)
            # c.append(nums[i-1][0]) # merged interval's start will be same as a[0]
            # c.append(max(nums[i-1][1], nums[i][1])) # end will be max of end of a and b
            # nums[i] = c
            result.append([nums[i-1][0], max(nums[i-1][1], nums[i][1])])
            nums[i] = [nums[i-1][0], max(nums[i-1][1], nums[i][1])]
            # c = []
        else:
            if i == 1:
                result.append(nums[i-1])
            else:
                result.append(nums[i])
        i += 1
    return (result)


def main():
    # nums = [[6,7], [2,4], [5,9]]
    # nums = [[1,4], [2,6], [3,5]]
    # nums = [[1,4], [2,5], [7,9]]
    print(mergeIntervals(nums))

main()