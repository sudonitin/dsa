def logic(s, nums):
  temp_subarray_length = 0
  window_sum = 0
  window_start = 0
  min_subarray_length = 0
  for i in range(len(nums) - 1):
    window_sum += nums[i]
    temp_subarray_length += 1
    while window_sum >= s: # one mistake only instead of looping through this I was using if condition
      min_subarray_length = min(min_subarray_length, temp_subarray_length) if min_subarray_length > 0 else temp_subarray_length
      window_sum -= nums[window_start]
      window_start += 1
      temp_subarray_length -= 1
  return min_subarray_length

def main():
  s = int(input())
  nums = list(map(int, input().split(', ')))
  result = logic(s, nums)
  print(result)

main()

'''
TEST CASES:
Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].


Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].


Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''