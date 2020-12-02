def logic(nums, k):
  window_start = 0
  count = 0
  max_length = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      count += 1
    while count > k:
      if nums[window_start] == 0:
        count -= 1
      window_start += 1
    max_length = max(max_length, i - window_start + 1)
  return max_length

def main():
  nums = list(map(int, input().split(', ')))
  k = int(input())
  result = logic(nums, k)
  print(result)
  return 1

main()