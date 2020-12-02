
def logic(arr, k):
  result_arr = []
  window_sum = 0
  window_start = 0
  max_sum = 0
  for i in range (len(arr) - 1):
    window_sum += arr[i]
    if i >= k - 1:
      max_sum = max(window_sum, max_sum)
      result_arr.append(window_sum)
      window_sum -= arr[window_start]
      window_start += 1
  return max_sum
  # return max(result_arr) -- this line can be improved by using a new max_sum variable that compares with window_sum

def main():
  k = int(input())
  nums = list(map(int, input().split(', ')))
  result = logic(nums, k)
  print(result)

main()