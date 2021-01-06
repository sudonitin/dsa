class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverseLL(head):
  prev = head
  curr = head.next

  while curr is not None:
    # print('testing', curr.value)
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  # print('last node', prev.value)
  head.next = None
  head = prev
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

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  print(reverseLL(head))
main()