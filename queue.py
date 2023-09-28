from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def __repr__(self):
        return f'{self.buffer}'
    
    def __str__(self):
        return self.__repr__()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

if __name__ == '__main__':
    queue_list =[]
    queue_list.insert(0, 132.21)
    queue_list.insert(0, 123.42)
    print(queue_list)

    print(queue_list.pop())

    print(queue_list.pop())

    q = deque()

    q.appendleft(5)
    q.appendleft(7)
    q.appendleft(10)
    q.appendleft(11)
    print(q)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    
    pq = Queue()

    pq.enqueue({
        'state' : 'Maharashtra',
        'rank' : 2
    })

    pq.enqueue({
        'state' : 'Gujarat',
        'rank' : 3
    })

    print(pq)

    pq.dequeue()
   
    print(pq)
