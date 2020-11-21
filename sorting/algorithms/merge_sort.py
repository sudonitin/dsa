'''sorting/algorithms/merge_sort.py

'''

def merge(arr):
  # print('inside merge', arr)
  l = 0
  r = len(arr)
  m = l + r // 2
  tempm = m
  result = []
  while l < tempm and m < r:
    if arr[l] < arr[m]:
      result.append(arr[l])
      l += 1
    else:
      result.append(arr[m])
      m += 1
  while l < tempm:
    result.append(arr[l])
    l+=1
  while m < r:
    result.append(arr[m])
    m += 1
  return result

def merge_sort(arr):
  if len(arr) > 1:
    m = len(arr) // 2
    firstHalf = merge_sort(arr[:m])
    secondHalf = merge_sort(arr[m:])
    res = merge(firstHalf+secondHalf)
    return res
  return arr

def main():
  arr = list(map(int, input().split(' ')))
  res = merge_sort(arr)
  print(res)
main()
# 64 25 12 22 11