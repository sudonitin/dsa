class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverseLL(head, p, q):
    prev = None
    curr = head
    count = 1
    while curr is not None:
        # print('testing', curr.value)    
        if p == 1 and count == 1:
            pnode = curr
            pprev = None
        if count == p - 1:
            prev = curr
            pprev = curr
            pnode = curr.next
            curr = curr.next
        elif count >= p and count <= q:
            # print("@@@@@", curr.value)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        elif count > q:
            qnode = prev
            qnext = curr
            break
        else:
            curr = curr.next
        count += 1

    # print('last node', prev.value)
    # head.next = None
    # head = prev
    # print(pnode.value, pprev.value, qnode.value, qnext.value)
    if p == 1:
        head = prev # prev is nothing but qnode
        pnode.next = curr # curr is nothing but qnode.next
    else:
        pprev.next = prev
        pnode.next = curr
    # print('new head = ', head.value)
    # print('head.next = ', head.next.value)

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
    print(reverseLL(head, 1, 5))


main()