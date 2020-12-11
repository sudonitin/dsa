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

def Dec11(nums):
  i,j = 0,1
  while j < len(nums):
    if nums[i] != nums[j]:
      i += 1
      nums[i] = nums[j]
    else:
      j += 1
  return i + 1

def main():
  nums = list(map(int, input().split(', ')))
  print('og', logic(nums))
  print('copied', otherLogic(nums))
  print('og', Dec11(nums))
  # print(result)
  return 1

main()