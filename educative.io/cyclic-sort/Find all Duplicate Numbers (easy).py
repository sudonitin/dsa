# n array size contains 1 to n nos along with duplicates
# find all duplicates without extra space

def logic(nums):
    result = []
    for i in range(len(nums)):
        while nums[i]-1 != i:
            temp = nums[i]
            if nums[temp-1] == nums[i]:
                result.append(temp)
                break
            nums[temp-1], nums[i] = nums[i], nums[temp-1]
    return result

def main():
    nums = list(map(int, input().split(", ")))
    print(logic(nums))

main()