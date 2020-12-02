# delete elements approach
def logic(nums):
  first = 0
  second = 1
  try:
    while nums[second]:
      if nums[first] == nums[second]:
        del(nums[second])
      else:
        first += 1
        second += 1
  except IndexError:
    return len(nums)
  except:
    print('Something else went wrong')
  # return nums

# w/o deleting elements
def otherLogic(nums):
  uniqueCount = 1
  i = 1
  while i < len(nums):
    if nums[uniqueCount - 1] != nums[i]:
      nums[uniqueCount] = nums[i]
      uniqueCount += 1
    i += 1
  return uniqueCount

def main():
  nums = list(map(int, input().split(', ')))
  # result = logic(nums)
  result = otherLogic(nums)
  print(result)
  return 1

main()