def logic(string, k):
  max_length = 0
  hash_map = {}
  window_start = 0
  distinct_char_count = 0
  for i in range(len(string)):
    if string[i] not in hash_map:
      hash_map[string[i]] = 1
    else:
      hash_map[string[i]] += 1
    if string[window_start] != string[i]:
      distinct_char_count += 1
    while distinct_char_count > k:
      hash_map[string[window_start]] -= 1
      if hash_map[string[window_start]] == 0:
        del hash_map[string[window_start]]
        window_start += 1
        distinct_char_count -= hash_map[string[window_start]]
      else:
        window_start += 1
    max_length = max(max_length, i - window_start + 1)
  return max_length

def main():
  string = list(input())
  k = int(input())
  result = logic(string, k)
  print(result)
  return 1

main()