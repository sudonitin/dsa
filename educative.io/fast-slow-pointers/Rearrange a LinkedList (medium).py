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
  print(opStr)

######################################################

def alter(head, center, evenLength, centerPrev):
  og = center
  if not evenLength:
    center = center.next
  head_first, head_second = head, center
  # print(head_first.value, head_second.value, centerPrev.value)
  # print(head_second.next.value)
  while head_first is not None and head_second.next is not None:
    # if head_first.next is None or head_second.next is None:
    #     break
    head_first_next = head_first.next
    # print('head_first_next ', head_first_next.value)
    # printLL(head)
    centerPrev.next = head_second.next
    # printLL(head)
    # print(head_second.next.value)
    # print('centerPrev.next', centerPrev.next.value)
    head_first.next = head_second
    # printLL(head)
    # print('head_first.next', head_first.next.value)
    head_second.next = head_first_next
    # printLL(head)
    # print('head_second.next', head_second.next.value)
    head_first = head_first_next
    # printLL(head)
    # print('head_first', head_first.value)
    head_second = centerPrev.next
    # printLL(head)
    # print('head_second', head_second.value)
  # print(og.next.value, 'og')
  if not evenLength:
    head_second.next = og
    og.next = None
  printLL(head)
  # temp = head
  # opStr = ''
  # while temp is not None:
  #   # print(temp.value, 'printing')
  #   if temp.next is None:
  #     opStr += str(temp.value)
  #   else:
  #     opStr += str(temp.value) + ' => '
  #   temp = temp.next
  # print(opStr)
######################################################

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  # head.next.next.next.next = Node(5)
  # head.next.next.next.next.next = Node(6)
  centerDetails = findCenterOfLL(head)
  # print('center details', centerDetails['evenLength'])
  # print(centerDetails['center'].value)
  # print(reverseSecondHalf(head, centerDetails['center'], centerDetails['evenLength'], centerDetails['centerPrev']))
  # print(centerDetails['centerPrev'].value)
  # print('Linked List before operations\n', printLL(head))
  reverseSecondHalf(head, centerDetails['center'], centerDetails['evenLength'],  centerDetails['centerPrev'])
  centerDetails['center'] = centerDetails['centerPrev'].next
  # print(printLL(head))
  alter(head, centerDetails['center'], centerDetails['evenLength'],  centerDetails['centerPrev'])
  # print(printLL(head))

main()