def ownLogic(nums, smallerSum):
    result = 0
    nums = sorted(nums)
    # print(nums)
    for i in range(1, len(nums)):
        targetSum = nums[i-1]
        p1,p2 = i,len(nums)-1
        while p1 < p2:
            if nums[p1]+nums[p2]+targetSum < smallerSum:
                result += p2-p1
                p1 += 1
            else:
                p2 -= 1
    return result

def main():
    nums = list(map(int, input().split(', ')))
    smallerSum = int(input())
    print(ownLogic(nums, smallerSum))
    return 1

main()