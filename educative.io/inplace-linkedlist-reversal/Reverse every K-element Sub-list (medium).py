class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def referredFromSolution(head, k):
    prev, curr = None, head
    while True:
        last_node_before_sublist = prev
        last_node_of_sublist = curr
        i = 0

        while curr is not None and i < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        last_node_of_sublist.next = curr
        if last_node_before_sublist is not None:
            last_node_before_sublist.next = prev
        else:
            head = prev
        
        if curr is None:
            break
        prev = last_node_of_sublist
    temp = head
    opStr = ""
    while temp is not None:
        # print(temp.value, 'printing')
        if temp.next is None:
            opStr += str(temp.value)
        else:
            opStr += str(temp.value) + " => "
        temp = temp.next
    return opStr

def reverseKLinkedList(head, k):
    prev, curr = None, head
    count = 0
    last_node_before_sublist = None
    last_node_of_sublist = curr

    while curr is not None:
        if count == k:
            # print(curr.value, "current")
            # change p and q
            # connect end pointers of sublist
            count = 0
            # print("last_node_of_sublist", last_node_of_sublist.value)
            last_node_of_sublist.next = curr
            if last_node_before_sublist is not None:
                last_node_before_sublist.next = prev
            else:
                head = prev
            last_node_before_sublist = last_node_of_sublist
            # print("last_node_before_sublist", last_node_before_sublist.value)
            last_node_of_sublist = curr
            prev = last_node_before_sublist
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            # print("current", curr.value)
        else:
            print(curr.value)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        count += 1
    
    if count < k:
        # print("last_node_of_sublist", last_node_of_sublist.value)
        last_node_of_sublist.next = curr
        if last_node_before_sublist is not None:
            # print("last_node_before_sublist", last_node_before_sublist.value)
            last_node_before_sublist.next = prev
        else:
            head = prev

    temp = head
    opStr = ""
    while temp is not None:
        # print(temp.value, 'printing')
        if temp.next is None:
            opStr += str(temp.value)
        else:
            opStr += str(temp.value) + " => "
        temp = temp.next
    return opStr

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)
    # print(reverseKLinkedList(head, 3))
    print(referredFromSolution(head, 3))
main()