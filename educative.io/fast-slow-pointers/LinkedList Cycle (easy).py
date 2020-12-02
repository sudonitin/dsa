class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def hasCycle(head):
  first = head
  second = head

  # With Try Except
  # try:
  #   while first.next and second.next.next:
  #     first = first.next
  #     second = second.next.next
  #     if first.value == second.value:
  #       return True
  # except AttributeError:
  #   return False

  # Without Try Except
  while second is not None and second.next  is not None:
      first = first.next
      second = second.next.next
      if first.value == second.value:
        return True
  
  return False

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  print("isCycle there..? " + str(hasCycle(head)))
  head.next.next.next.next.next = head
  print("isCycle there? " + str(hasCycle(head)))

main()