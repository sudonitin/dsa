''' selection_sort.py
############### NOTES ###############
=> From GFG
  The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

  1) The subarray which is already sorted.
  2) Remaining subarray which is unsorted.

  In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

  ** Time Complexity: O(n2) as there are two nested loops.

  ** Auxiliary Space: O(1)
  The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

=> My Note
  - No need to maintain different arrays, this can be done in-place
  - Simply swap the minimum number with current index
'''

def selection_sort(arr):
  for i in range(len(arr)):
    temp = arr[i]
    for j in range(i, len(arr)):
      temp = arr[j] if temp > arr[j] else temp
    if temp != arr[i]:
      tempIndex = arr.index(temp)
      arr[i], arr[tempIndex] = arr[tempIndex], arr[i]
  print(arr)
  return 1

def main():
  arr = list(map(int, input().split(' ')))
  selection_sort(arr)

main()

# input examples
# 64 25 12 22 11