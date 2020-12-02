class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

# find length of cycle
def lengthOfCycle(head):
  slow, fast = head, head
  length = 0
  cycleDetected = False
  iteration = 0
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow.value == fast.value:
      cycleDetected = True
      iteration += 1
    if cycleDetected and iteration < 2:
      length += 1
    elif iteration == 2:
      return length

# find starting node
def startNode(head, length):
  first = head
  second = head
  for i in range(length):
    second = second.next
  while second is not None and second.next is not None:
    if first.value == second.value:
      return first.value
    first = first.next
    second = second.next

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  # head.next.next.next.next.next = head
  head.next.next.next.next.next = head.next.next
  length = lengthOfCycle(head)
  print("start node is " + str(startNode(head, length)))

main()