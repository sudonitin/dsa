# 1 to n nos exists in array along with duplicates
# find all missing numbers

def logic(nums):
    result = []
    for i in range(len(nums)):
        while nums[i]-1 != i:
            temp = nums[i]
            if nums[temp-1] == nums[i]:
                break
            nums[temp-1], nums[i] = nums[i], nums[temp-1]
    for i in range(len(nums)):
        if nums[i]-1 != i:
            result.append(i+1)
    return result

def main():
    nums = list(map(int, input().split(", ")))
    print(logic(nums))

main()