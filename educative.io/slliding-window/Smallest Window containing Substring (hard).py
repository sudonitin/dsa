def logic(string, pattern):
  patternLength = len(pattern)
  tempLength = 0
  windwo_start = 0
  result = ''
  hash_map = {}
  for i in pattern:
    hash_map[i] = 0
  for window_end in range(len(string)):
    result += string[window_end]
    if string[window_end] in hash_map:
      hash_map[string[window_end]] += 1
    
  return 1

def main():
  string = list(input())
  pattern = list(input())
  result = logic(string, pattern)
  print(result)
  return 1

main()

'''
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
'''