class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked List is empty!')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for i in data_list:
            self.insert_at_end(i)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        elif index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                count += 1
                itr = itr.next

    def insert_at(self, index, value):
        itr = self.head
        count = 0
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index provided!')
        if index == 0:
            node = Node(value, itr)
            self.head = node
        elif 0 < index < self.get_length():
            while itr:
                if count == index - 1:
                    nex = itr.next
                    itr.next = Node(value, nex)
                itr = itr.next
                count += 1
        else:
            while itr.next is not None:
                itr = itr.next
            itr.next = Node(value, None)

    def insert_after_value(self, data_after, data_add):
        itr = self.head
        while itr:
            if itr.data == data_after:
                nex = itr.next
                itr.next = Node(data_add, nex)
                return
            itr = itr.next
        raise Exception('The given value is not in the Linked List')

    def remove_by_value(self, value):
        itr = self.head
        count = 0
        if itr.data == value and self.get_length() == 1:
            self.head = None
            return
        elif itr.data == value:
            self.head = itr.next
            return
        while itr.next is not None:
            curr = itr
            if itr.next.data == value:
                curr.next = itr.next.next
                return
            itr = itr.next
        raise Exception('The value to be removed is not in the Linked List')

    def remove_duplicates(self):
        print('In the remove duplicate function!')
        itr = self.head
        while itr.next is not None:
            if itr.data == itr.next.data:
                itr.next = itr.next.next
            else:
                itr = itr.next

    def is_palindrome(self):
        if self.head is None:
            return False
        m, itr = [], self.head
        while itr:
            m.append(itr.data)
            itr = itr.next
        print(m)
        for i in range(0, (len(m) // 2)):
            if m[i] != m[len(m) - 1 - i]:
                return False
        return True

    def remove_all_elements(self, data):
        if self.head is None:
            return
        itr = self.head
        while data == itr.data:
            self.head = itr.next
            if itr.next is None:
                return
            itr = itr.next
        while itr.next is not None:
            if itr.next.data == data:
                itr.next = itr.next.next
            else:
                itr = itr.next

    def getdecimalvalue(self):
        m = []
        if self.head is None:
            return self.head
        itr = self.head
        while itr:
            m.append(itr.data)
            itr = itr.next
        m, c, sum = m[::-1], 0, 0
        while c < len(m):
            print(sum)
            sum += m[c] * 2 ** c
            c += 1
        return sum

    def middleNode(self):
        if self.head is None:
            return self.head
        count, itr, s = 0, self.head, 0
        while itr:
            count += 1
            itr = itr.next
        itr = self.head
        while itr:
            if count % 2 == 0 and s == (count // 2):
                self.head = itr
                return
            if count % 2 != 0 and s == ((count + 1) // 2) - 1:
                self.head = itr
                return
            s += 1
            itr = itr.next

    def removenodes_stricly_greater(self):
        if self.head is None:
            return
        itr = self.head
        while itr.data < itr.next.data:
            head = itr.next
            itr = itr.next
        while itr.next is not None:
            if itr.data < itr.next.data:
                if itr.next.next is not None:
                    itr.next = itr.next.next
                else:
                    itr.next = None
            else:
                itr = itr.next
        return

    def remove_small_nodes_keep_strictly_greater(self):
        if self.head is None:
            return
        itr = self.head
        m = []
        while itr.data < itr.next.data:
            self.head = itr.next
            itr = self.head

        while itr.next is not None:


if __name__ == '__main__':
    l6 = linkedlist()
    #l6.insert_values([138,466,216,67,642,978,264,136,463,331,60,600,223,275,856,809,167,101,846,165,575,276,409,590,733,200,839,515,852,615,8,584,250,337,537,63,797,900,670,636,112,701,334,422,780,552,912,506,313,474,183,792,822,661,37,164,601,271,902,792,501,184,559,140,506,94,161,167,622,288,457,953,700,464,785,203,729,725,422,76,191,195,157,854,730,577,503,401,517,692,42,135,823,883,255,111,334,365,513,338,65,600,926,607,193,763,366,674,145,229,700,11,984,36,185,475,204,604,191,898,876,762,654,770,774,575,276,165,610,649,235,749,440,607,962,747,891,943,839,403,655,22,705,416,904,765,905,574,214,471,451,774,41,365,703,895,327,879,414,821,363,30,130,14,754,41,494,548,76,825,899,499,188,982,8,890,563,438,363,32,482,623,864,161,962,678,414,659,612,332,164,580,14,633,842,969,792,777,705,436,750,501,395,342,838,493,998,112,660,961,943,721,480,522,133,129,276,362,616,52,117,300,274,862,487,715,272,232,543,275,68,144,656,623,317,63,908,565,880,12,920,467,559,91,698])
    l6.insert_values([5, 22, 13, 3, 5, 3, 2, 8])
    l6.remove_small_nodes_keep_strictly_greater()
    l6.print()
