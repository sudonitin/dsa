def ownLogic(nums):
    nums.sort(key=lambda x:x[0])
    i = 1
    while i<len(nums):
        if nums[i][0] <= nums[i-1][1]:
            return False
        i += 1
    return True

def main():
    nums = [[4,5], [2,3], [3,6]]
    print(ownLogic(nums))

main()