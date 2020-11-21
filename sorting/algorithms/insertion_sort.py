'''sorting/algorithms/insertion_sort.py

############### NOTES ###############
=> GFG
  Time Complexity: O(n*2)

  Auxiliary Space: O(1)

=> My Notes
- To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

'''

def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i
    key = arr[i]
    while j > 0 and arr[j-1] > key:
      arr[j] = arr[j-1]
      j -= 1
    arr[j] = key
  print(arr)
  return 1

def main():
  arr = list(map(int, input().split(' ')))
  insertion_sort(arr)
  return

main()