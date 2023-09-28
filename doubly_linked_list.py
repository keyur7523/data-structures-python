class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class double_linked_list:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('The Doubly Linked List is empty!')
            return
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '<==>'
            itr = itr.next
        print(dllstr)

    def insert_at_beginning(self, data):
        node = Node(None, data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(self.head,data,None)
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = Node(itr,data,None)

    def insert_values(self, data_list):
        for i in data_list:
            self.insert_at_end(i)

    def get_length(self):
        count, itr = 0, self.head
        while itr:
            count += 1
            itr = itr.next
        #print(f'The length of the doubly linked list is {count}.')
        return count

    def remove_at_index(self, data):
        count, itr = 0, self.head
        if 0 > data or data >= self.get_length():
            raise Exception('The index is invalid!')
        elif data == 0:
            if self.get_length() == 1:
                self.head = None
                return
            self.head = itr.next
            return
        while itr:
            if count == data:
                itr = itr.prev
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if 0 > index or index > self.get_length():
            raise Exception('The index is invalid!')
        if index == 0:
            self.head = Node(None, data, self.head)
            return
        itr, count = self.head, 0
        while itr:
            print(count)
            if count == index:
                itr = itr.prev
                itr.next = Node(itr, data, itr.next)
                return
            itr = itr.next
            count += 1


if __name__ == '__main__':
    l3 = double_linked_list()
    l3.insert_values(['apple','mango','banana','grape'])
    l3.print()
    #l3.remove_at_index(1)
    l3.insert_at(4,'cherry')
    l3.print()