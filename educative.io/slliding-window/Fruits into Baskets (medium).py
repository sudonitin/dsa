def logic(fruitTrees):
  hash_map = {}
  max_length = 0
  window_start = 0
  # "i" is always sliding window_end
  for window_end in range(len(fruitTrees)):
    if fruitTrees[window_end] not in hash_map:
      hash_map[fruitTrees[window_end]] = 0
    hash_map[fruitTrees[window_end]] += 1
    # shrinking the window when distinct characters are more than "k"
    while len(hash_map) > 2:
      hash_map[fruitTrees[window_start]] -= 1
      if hash_map[fruitTrees[window_start]] == 0:
        del hash_map[fruitTrees[window_start]]
      window_start += 1
    # calculate max_length based on positions of window_start and window_end
    max_length = max(max_length, window_end - window_start + 1)

  return max_length

def main():
  fruitTrees = list(map(str, input().split(", ")))
  result = logic(fruitTrees)
  print(result)
  
main()