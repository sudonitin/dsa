'''sorting/algorithms/quick_sort.py

 QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
 The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.



'''

def partition(arr, low, high):
  i = low - 1
  for j in range(low, high+1):
    if arr[j] < arr[high]:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1

def quick_sort(arr, low, high):
  if low < high:
    pivotIndex = partition(arr, low, high)
    quick_sort(arr, low, pivotIndex-1)
    quick_sort(arr, pivotIndex+1, high)
  return arr

def main():
  arr = list(map(int, input().split(' ')))
  res = quick_sort(arr, 0, len(arr)-1)
  print(res)
main()
# 64 25 12 22 11