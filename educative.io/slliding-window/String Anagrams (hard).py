#khudka logic
def logic(string, pattern):
  patternSum = 0
  patternLength = len(pattern)
  for i in pattern:
    patternSum += ord(i)
  window_start = 0
  window_sum = 0
  result = []
  for window_end in range(len(string)):
    window_sum += ord(string[window_end])
    if window_end - window_start + 1 == patternLength:
      if window_sum == patternSum:
        result.append(window_start)
      window_sum -= ord(string[window_start])
      window_start += 1
  return result

def main():
  string = list(input())
  pattern = list(input())
  result = logic(string, pattern)
  print(result)
  return 1

main()