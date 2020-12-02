def logic(nums, target):
  start = 0
  end = len(nums) - 1
  # result = [] # this is not needed
  while start <= end:
    if nums[start] + nums[end] == target:
      # result.append(start)
      # result.append(end)
      # break
      return [start, end]
    elif nums[start] + nums[end] > target:
      end -= 1
    else:
      start += 1

  return [-1, -1]

def main():
  nums = list(map(int, input().split(', ')))
  target = int(input())
  result = logic(nums, target)
  print(result)
  return 1

main()