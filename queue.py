class queue:
    def __init__(self, n):
        self.q = [None]*n
        self.front = self.rear = 0
        self.size = n

    def enqueue(self, data):
        if self.size == self.rear:
            print('Queue Full')
            return
        self.q[self.rear] = data
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print('This foo empty')
            return
        tmp = self.q
        ## List unpacking using *
        ## Extending the list a null each time so index has a placeholder
        ret, *self.q = tmp + [None]
        self.rear -= 1
        return ret

    ## simple display method cheeky end=''

    def display(self):
        if self.front == self.rear:
            print('Empty')
            return
        [print(x, end='-->') for x in self.q[:self.rear]]
        print('None')

    ## front() is giving me a python lib error 
    ## uh oh

    def front(self):
        if self.front == self.rear:
            print('Nah')
            return
        return self.q[self.front]
