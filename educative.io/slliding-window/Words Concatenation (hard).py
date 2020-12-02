# KHUDKA LOGIC
def logic(string, words):
  allWords = ''
  allWordsSum = 0
  singleWordLength = len(words[0])
  for i in words:
    # print(sum(map(ord, i)))
    allWords += i
  # print('allwords', allWords)
  for i in allWords:
    allWordsSum += ord(i)
  # print('all sum', allWordsSum)
  allWordsLength = len(allWords)
  window_start = 0
  window_sum = 0
  result = []
  for window_end in range(len(string)):
    window_sum += ord(string[window_end])
    # print(window_sum, 'win sum')
    if window_end - window_start + 1 == allWordsLength:
      if window_sum == allWordsSum:
        result.append(window_start)
      # print(string[window_start:singleWordLength])
      # print(sum(bytearray(string[window_start:singleWordLength])))
      window_sum -= sum(map(ord, string[window_start:singleWordLength]))
      # print(window_sum, 'sub sum')
      # print("testing", window_sum)
      window_start += singleWordLength
      # print(window_start, 'start')
  return result

def main():
  string = input()
  words = list(map(str, input().split(', ')))
  result = logic(string, words)
  print(result)
  return 1

main()
