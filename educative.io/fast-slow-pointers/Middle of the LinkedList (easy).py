class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def khudkaLogic(head): # extra condition was not required
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fastTemp = fast
    fast = fast.next.next
    slowTemp = slow
    slow = slow.next
  if fastTemp.next is not None:
    return slowTemp.next.value
  return slowTemp.value

# awesome logic
def givenLogic(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
  return slow.value

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  print(khudkaLogic(head))
  print(givenLogic(head), "given")
  head.next.next.next.next.next = Node(6)
  print(khudkaLogic(head))
  print(givenLogic(head), "given")
  head.next.next.next.next.next.next = Node(7)
  print(givenLogic(head), "given")
  print(khudkaLogic(head))
  return

main()