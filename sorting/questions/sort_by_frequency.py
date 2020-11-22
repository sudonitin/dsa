# https://www.geeksforgeeks.org/sort-elements-by-frequency/

def sort(arr):
  freq = {}
  for i in (arr):
    freq[i] = 0
  for i in arr:
    freq[i] += 1
  res = [k for k,v in sorted(freq.items(), key=lambda item:item[1], reverse=True)]
  print(res)

def main():
  arr = list(map(int, input().split(', ')))
  sort(arr)

main()
# 64 25 12 22 11
# 8 8 8 5 5 2 2 6 -1 9999999