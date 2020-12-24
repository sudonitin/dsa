def ownLogic(nums, closestSum):
    mainSum = closestSum
    nums = sorted(nums)
    while mainSum >= 0:
        mainSum -= 1
        for i in range(1, len(nums)):
            targetSum = nums[i-1]
            p1,p2 = i,len(nums)-1
            while p1 < p2:
                if nums[p1]+nums[p2]+targetSum > mainSum:
                    p2 -= 1
                elif nums[p1]+nums[p2]+targetSum == mainSum:
                    p1 += 1
                    p2 -= 1
                    # return [targetSum, nums[p1], nums[p2]]
                    return nums[p1]+nums[p2]+targetSum
                else:
                    p1 += 1
    return -1

def main():
    nums = list(map(int, input().split(', ')))
    closestSum = int(input())
    print(ownLogic(nums, closestSum))
    return 1

main()