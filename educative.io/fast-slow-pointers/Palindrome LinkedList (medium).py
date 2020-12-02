'''
----------- conditions ------------
1. constant space
2. input LinkedList should be in the original form once the algorithm is finished
3. Algorithm should have O(N) time complexity

----------- Steps ------------
1. find center of LL
2. reverse 2nd part
3. compare 1st & 2nd part
4. reverse 2nd part
'''

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

######################################################

def findCenterOfLL(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    temp = slow
    slow = slow.next
    fast = fast.next.next
  evenLength = True
  if fast is None:
    evenLength = True
    centerPrev = temp
  else:
    evenLength = False
    centerPrev = temp
  # print(temp.value)
  return { 'center': slow, 'evenLength': evenLength, 'centerPrev': centerPrev }

######################################################

def reverseSecondHalf(head, center, evenLength, centerPrev):
  # print(center.value, 'center')
  # og = center
  if not evenLength:
    og = center
    center = center.next
  else:
    og = centerPrev
  prev = center
  curr = center.next

  while curr is not None:
    # print('testing', curr.value)
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  # print('last node', prev.value)
  # head.next = None
  # head = prev
  og.next = prev
  center.next = None
  # print('new head = ', head.value)
  # print('head.next = ', head.next.value)

  temp = head
  opStr = ''
  while temp is not None:
    # print(temp.value, 'printing')
    if temp.next is None:
      opStr += str(temp.value)
    else:
      opStr += str(temp.value) + ' => '
    temp = temp.next
  return opStr

######################################################

def isLLpalindrome(head, center, evenLength):
  if not evenLength:
    center = center.next
  temp = head
  while center is not None:
    if temp.value != center.value:
      # print(False)
      return False
    center = center.next
    temp = temp.next
  # print(True)
  return True

######################################################

def printLL(head):
  temp = head
  opStr = ''
  while temp is not None:
    # print(temp.value, 'printing')
    if temp.next is None:
      opStr += str(temp.value)
    else:
      opStr += str(temp.value) + ' => '
    temp = temp.next
  return (opStr)

######################################################

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(2)
  head.next.next.next = Node(1)
  # head.next.next.next.next = Node(1)
  # head.next.next.next.next.next = Node(6)
  centerDetails = findCenterOfLL(head)
  # print('center details', centerDetails['evenLength'])
  # print(centerDetails['center'].value)
  # print(reverseSecondHalf(head, centerDetails['center'], centerDetails['evenLength'], centerDetails['centerPrev']))
  # print(centerDetails['centerPrev'].value)
  print('Linked List before operations\n', printLL(head))
  reverseSecondHalf(head, centerDetails['center'], centerDetails['evenLength'],  centerDetails['centerPrev'])
  # print('Linked List after 1st, 2nd half reverse\n', printLL(head))
  centerDetails['center'] = centerDetails['centerPrev'].next
  print(isLLpalindrome(head, centerDetails['center'], centerDetails['evenLength']))
  reverseSecondHalf(head, centerDetails['center'], centerDetails['evenLength'],  centerDetails['centerPrev'])
  # print('Linked List after 2nd, 2nd half reverse\n', printLL(head))
  print('Linked List after operations\n', printLL(head))

main()