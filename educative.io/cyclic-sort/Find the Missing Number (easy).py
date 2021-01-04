# Given 0 to n+1 in an array of size n find missing number

# 1 iteration needed => TC: O(n)
# missing_number = n(n+1)/2 - sum(given_array)
def arithmeticApproach(nums):
    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)

# 2 iterations needed => TC: O(n)
# 1) arrange elements acc to index-1 (apply cyclic sort) 
#   1.1) skip if 0 is the element 
# 2) find index with element 0 return index + 1
def cyclicSortApproach(nums):
    for i in range(len(nums)):
        while nums[i] !=0 and nums[i] != i+1:
            temp = nums[i]
            nums[i], nums[temp-1] = nums[temp-1], nums[i]
    for i in range(len(nums)):
        if nums[i] == 0:
            return i + 1

def main():
    nums = list(map(int, input().split(", ")))
    print("Arithmetic soln", arithmeticApproach(nums))
    print("Cyclic Sort soln", cyclicSortApproach(nums))
    return

main()
