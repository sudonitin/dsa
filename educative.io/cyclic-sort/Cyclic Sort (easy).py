# 1 to n is given
# swap number with index = number - 1 => soln
# eg
# i/p = [3, 1, 5, 4, 2]
# o/p = [1, 2, 3, 4, 5]
# TC = O(n)+O(n-1) = O(n) 
# SC = o(1)

def ownLogic(nums):
    for i in range(len(nums)): # O(n)
        while nums[i]-1 != i: # O(n-1)
            temp = nums[i]
            nums[temp-1], nums[i] = nums[i], nums[temp-1]
    return nums

def main():
    nums = list(map(int, input().split(", ")))
    print(ownLogic(nums))
main()