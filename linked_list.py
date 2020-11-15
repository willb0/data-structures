class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def addfront(self, val):
        if self.head:
            n = Node(val)
            n.next = self.head
            self.head = n
        else:
            self.head = Node(val)

    def print(self):
        tmp = self.head
        while(tmp.next != None):
            print('%d -->' % tmp.val, end=' ')
            tmp = tmp.next
        print('%d --> None' % tmp.val)

    def addlast(self, val):
        if self.head == None:
            self.addfront(val)
        else:
            tmp = self.head
            while(tmp.next != None):
                tmp = tmp.next
            tmp.next = Node(val)

    def ins_after(self, key, val):
        tmp = self.head
        while(tmp.next != None):
            if(tmp.val == key):
                n = Node(val)
                n.next = tmp.next
                tmp.next = n
                return
            tmp = tmp.next
        if(tmp.val == key):
            tmp.next = Node(val)
            return
        print('Key Not Found')

    def ins_before(self, key, val):
        tmp = self.head
        if not tmp:
            return None
        if tmp.val == key:
            self.head = Node(val, tmp)
            return
        prev = None
        curr = tmp
        while(curr != None and curr.val != key):
            prev = curr
            curr = curr.next
        if curr:
            n = Node(val)
            n.next = curr
            prev.next = n
        else:
            print('Key Not Found')

    def delete(self, key):
        tmp = self.head
        if not tmp:
            return "Error"
        if tmp.val == key:
            self.head = tmp.next
            return
        prev = None
        curr = tmp
        while curr and curr.val != key:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
        else:
            return "Error"

    def clone(self):
        clone = linked_list()
        tmp = self.head
        clone.head = Node(tmp.val, None)
        tmp2 = clone.head
        while(tmp.next):
            tmp = tmp.next
            tmp2.next = Node(tmp.val, None)
            tmp2 = tmp2.next
        return clone


ll = linked_list()
ll.addfront(5)
ll.addlast(8)
ll.addfront(3)
ll.print()
ll.ins_before(3, 10)
ll.print()
ll.delete(8)
ll.print()
ll2 = ll.clone()
ll2.print()
print(hex(id(ll)), hex(id(ll2)))
del ll
