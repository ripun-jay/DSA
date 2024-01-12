class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head= None):
        self.head = head

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            # print(itr.data)
            llstr+= str(itr.data) + "--->"
            itr = itr.next
        print(llstr)


    def insert_values(self, data_list):
        # just want LL of passed list thus making sure head is None
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
            return

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        """if index == self.get_length():
            self.insert_at_end(data)"""
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    """ll.insert_at_beginning(4)
    ll.insert_at_beginning(3)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.insert_at_end("b")
    ll.insert_at(5,8)
    ll.insert_at(6,9)
    ll.insert_at(7,10)
    print(ll.get_length())
    ll.insert_at(3,10)"""

    ll.insert_values(["a", "b", "c", "d"])
    ll.insert_at(4,5)   #solve it why it is iterate beyond end
    ll.remove_at(4)      #not able to remove last element --> solved how? last
    ll.remove_at(2)
    ll.remove_at(0)

    ll.print()

