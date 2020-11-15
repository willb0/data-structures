from linked_list import Node

class stacc:
    def __init__(self):
        self.top = Node()

    def push(self, val):
        self.top = Node(val,self.top)
    def pop(self):
        tmp = self.top
        self.top = self.top.next
        return tmp
    def peek(self):
        tmp = self.top
        while(tmp):
            print('%a -->' % tmp.val,end='')
            tmp = tmp.next
s = stacc()
[s.push(x) for x in range(10)]
s.peek()
