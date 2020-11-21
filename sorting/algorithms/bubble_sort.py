'''sorting/algorithms/bubble_sort.py

############### NOTES ###############

=> GFG
  Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

  Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

  Auxiliary Space: O(1)

  Sorting In Place: Yes
  

=> My Note
  - biggest element will always be pushed to the last position (ascending order)
'''

def bubble_sort(arr):

  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
  print('Bubble Sorting')
  print(arr)
  return 1

def main():
  arr = list(map(int, input().split(' ')))
  bubble_sort(arr)

main()
# 64 25 12 22 11