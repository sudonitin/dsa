def khudkaLogic(num):
  hashMap = {}
  result = 0
  temp = num
  while result != 1:
    # temp = num
    result = 0
    while temp != 0:
      result += temp % 10 * temp % 10
      temp = temp // 10
    temp = result
    if result in hashMap:
      print(result, 'ff')
      return False
    hashMap[result] = 1
  

  return True

def main():
  num = int(input())
  result = khudkaLogic(num)
  print(result)

main()