# KHUDKA LOGIC
def logic(pattern, string):
  patternSum = 0
  for i in pattern:
    patternSum += ord(i)
  window_start = 0
  window_sum = 0
  patternLength = len(pattern)
  resultFlag = False
  for window_end in range(len(string)):
    window_sum += ord(string[window_end])
    if window_end - window_start + 1 == patternLength:
      if window_sum == patternSum:
        resultFlag = True
        break
      else:
        window_sum -= ord(string[window_start])
        window_start += 1
  return resultFlag



def main():
  pattern = list(input())
  string = list(input())
  result = logic(pattern, string)
  print(result)
  return 1

main()