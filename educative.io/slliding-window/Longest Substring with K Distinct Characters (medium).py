
# WRONG SOLUTION FOR this case String="cbbebi", K=3
# def brute_force(k, nums):
#   distinct_count = 0
#   window = []
#   longest_substring_length = 0
#   for i in range(len(nums) - 1):
#     if nums[window_end] not in window:
#       distinct_count += 1
#       if distinct_count > k:
#         # print('**', len(window))
#         longest_substring_length = max(len(window), longest_substring_length) if longest_substring_length > 0 else len(window)
#         distinct_count = 0
#         window = []
#       else:
#         # print('--', nums[window_end], i)
#         window.append(nums[window_end])
#     else:
#       # print('##', nums[window_end], i)
#       window.append(nums[window_end])
#   return longest_substring_length

# OPTIMIZED SOLUTION
def mainLogic(k, nums):
  hash_map = {}
  max_length = 0
  window_start = 0
  # "i" is always sliding window_end
  for window_end in range(len(nums)):
    if nums[window_end] not in hash_map:
      hash_map[nums[window_end]] = 0
    hash_map[nums[window_end]] += 1
    # shrinking the window when distinct characters are more than "k"
    while len(hash_map) > k:
      hash_map[nums[window_start]] -= 1
      if hash_map[nums[window_start]] == 0:
        del hash_map[nums[window_start]]
      window_start += 1
    # calculate max_length based on positions of window_start and window_end
    max_length = max(max_length, window_end - window_start + 1)

  return max_length

    

def main():
  k = int(input())
  nums = list(input())
  # result = brute_force(k, nums)
  result = mainLogic(k, nums)
  print(result)
  return 1

main()