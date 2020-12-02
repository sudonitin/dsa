def logic(string):
  window_start = 0
  max_length = 0
  hash_map = {}
  for window_end in range(len(string)):
    if string[window_end] not in hash_map:
      hash_map[string[window_end]] = 0
      hash_map[string[window_end]] += 1
    else:
      window_start = window_end
      hash_map[string[window_end]] = 1
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

def main():
  string = list(input())
  result = logic(string)
  print(result)

main()