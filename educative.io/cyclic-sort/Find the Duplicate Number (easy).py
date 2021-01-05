# n+1 array size contains 1 to n nos along with duplicate
# find duplicate without extra space

def logic(nums):
    result = []
    for i in range(len(nums)):
        while nums[i]-1 != i:
            temp = nums[i]
            if nums[temp-1] == nums[i]:
                return temp
            nums[temp-1], nums[i] = nums[i], nums[temp-1]
    return None

def main():
    nums = list(map(int, input().split(", ")))
    print(logic(nums))

main()