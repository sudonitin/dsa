def ownLogic(nums):
    result = []
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            targetSum = -1 * nums[i-1]
            p1,p2 = i,len(nums)-1
            tempResult = []
            while p1 < p2:
                if nums[p1]+nums[p2] > targetSum:
                    p2 -= 1
                elif nums[p1]+nums[p2] == targetSum:
                    tempResult.append(-1*targetSum)
                    tempResult.append(nums[p1])
                    tempResult.append(nums[p2])
                    result.append(tempResult)
                    tempResult = []
                    p1 += 1
                    p2 -= 1
                else:
                    p1 += 1
    return result

def main():
    nums = list(map(int, input().split(', ')))
    print(ownLogic(nums))
    return 1

main()