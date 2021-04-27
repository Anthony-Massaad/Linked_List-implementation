class Node:
    def __init__(self, item):
        self.item = item   
        self.next = None

class LinkedList:
    def __init__(self, lst=None) -> None:
        """Initialize the empty linked List
           added list, will iterate through and add items to linked list
        
        """
        self._head = None
        self._size = 0
        if lst is not None: 
            for items in lst:
                self.append(items)

    def __len__(self) -> int:
        """Return the number of items in this bag."""
        return self._size

    def __str__(self) -> str:
        """
        Print Linked list
        """
        if self._head is None:
            return 'None'
        curr = self._head
        items = []
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '->'.join(items)

    def remove(self, item=None):
        """
        Remove specified item and return that item.
        If the head is none, meaning no elements in linked list, it will return none
        if no item provided, will remove the first element and return the first element 
        otherwise, will remove specifed element if exist and return specified element
        """
        if self._head is None:
            return None
        if item is None:
            value = self._head.item
            temp = self._head.next
            self._head = temp
            self._size -= 1
            return value
        curr = self._head
        prev = None
        while curr is not None:
            if curr.item == item:
                value = curr.item
                if prev is None:
                    self._head = curr.next
                else:
                    prev.next = curr.next
                self._size -= 1
                return value
            prev = curr
            curr = curr.next
        raise ValueError("{0} is not in the list".format(item))

    def is_empty(self) -> bool:
        """
        Boolean check if the linked list is empty
        """
        return self._head is None

    def pop(self, index=0) -> None:
        """
        pop specified index and return the element at that index
        if the linked list is empty, so head is none, will just return none
        will raise error is the index is invalid
        otherwise, no index provided assumes index 0 and pops the first element
        otherwise, will pop at that speiciied index
        """
        if self._head is None:
            return None
        if index >= self._size or index < 0:
            raise IndexError('index out of bounds')

        if index == 0:
            value = self._head.item
            temp = self._head.next
            self._head = temp
            self._size -= 1
            return value
        else: 
            counter = 0
            curr = self._head
            prev = None
            while curr is not None:
                if counter == index:
                    value = curr.item
                    temp = curr.next
                    prev.next = temp
                    self._size -= 1
                    return value
                prev = curr
                curr = curr.next
                counter += 1      

    def indexOf(self, item)->int:
        """
        Get the index of a specifed item
        If item doesn't exist, will raise an error
        """
        counter = 0
        curr = self._head
        while curr is not None:
            if curr.item == item:
                return counter
            counter += 1
            curr = curr.next
        raise ValueError("{0} is not in the list".format(item))

    def add(self, item)->None:
        """
        create a new head and shift everything to the right
        """
        if self._head is None:
            self._head = Node(item)
            self._size += 1
            return 
        temp = Node(item)
        temp.next = self._head
        self._head = temp
        self._size += 1

    def insert(self, item, index) -> None:
        """
        Will insert a specifed item to a specified index
        if the index is invalid, will raise an error
        otherwise, will inset new node
        """

        curr = self._head
        counter = 0
        if index < 0:
            raise IndexError("negative index")
        else:
            if index == 0:
                self.add(item)
            elif index >= self._size:
                self.append(item)
            else:
                while curr.next is not None and counter < index - 1:
                    curr = curr.next
                    counter += 1
                temp = Node(item)
                temp.next = curr.next
                curr.next = temp
                self._size += 1

    def __contains__(self, item) -> bool:
        """
        constains method if item is in linked list
        True if so, otherwise False
        Ex: 
        linked = 93->40->83
        >>> 93 in linked
        True
        >>> 20 in linked
        False 
        """
        curr = self._head
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False    

    def append(self, item) -> None:
        """
        append to the rear of the linked list
        """
        if self._head is None:
            self._head = Node(item)
            self._size += 1
            return 
        curr = self._head
        new_node = Node(item)
        previous = None
        while curr is not None:
            previous = curr
            curr = curr.next
        previous.next = new_node
        self._size += 1

    def reverse(self)->None:
        """
        Reverse the linked list in opposite order
        """
        if self._head is None:
            return None
        curr = self._head
        prev = None
        while curr is not None: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self._head = prev
    
    def peekLast(self):
        """
        If head is None, will return None
        otherwise, will return the last element in the linked list
        """
        if self._head is None:
            return None
        curr = self._head
        prev = None
        while curr is not None:
            prev = curr
            curr = curr.next
        return prev.item
    
    def peekHead(self):
        """
        If the head is None, will return none
        otherwise, will reutnr the first element in the linked list 
        """
        if self._head is None:
            return None
        return self._head.item
    
    def clear(self)->None:
        """
        Clears the linked lsit
        """
        self._head = None
    
    def removeLast(self):
        """
        Remove the last element in the linked list 
        """
        if self._head is None:
            return None
        value = self.pop(self._size - 1)
        return value
    
    def createAsList(self)->list:
        """
        Generate a list of the linked list
        """
        lst = []
        if self._head is None:
            return lst
        curr = self._head
        while curr is not None:
            lst.append(curr.item)
            curr = curr.next
        return lst

    def copy(self):
        """
        Generate a new linked list that is a copy of the original one
        """
        new_linkedList = LinkedList(self.createAsList())
        return new_linkedList

    def replace(self, index, item):
        """
        Replace a specifed index with a specifed item
        will just add to the head if the head is None
        will raise an index error if the index is invalid
        otherwise, will search and change the index item
        """
        if self._head is None:
            self.add(item)
            return
        if index >= self._size or index < 0:
            raise IndexError('Index out of bounds')
        counter = 0
        curr = self._head
        while curr is not None:
            if counter == index:
                curr.item = item
                return
            curr = curr.next
            counter += 1

    def get(self, index: int):
        """
        Get a value of a specifed index otherwise None
        Will raise error is the index is out of Bounds
        """
        if index >= self._size or index < 0:
            raise IndexError('Index out of bounds')
        counter = 0
        curr = self._head
        while curr is not None: 
            if counter == index: 
                return curr.item
            curr = curr.next
            counter += 1
        return None
    
    def __getitem__(self, arg: int):
        """
        Allow the user to get the index using the [] method
        Ex: linked = 93->40->83
        >>> linked[0]
        93
        >>> linked[10]
        index out of bounds
        """
        return self.get(arg)

#Main Method for Testing
"""
if __name__ in "__main__":
    linked = LinkedList()
    print(linked)
    print(linked.is_empty())
    for i in range(10,110,10):
        linked.append(i)
        print(linked)
    print(len(linked))
    for i in range(30,80, 10):
        linked.remove(i)
        print(linked)
    print(len(linked))
    print(20 in linked)
    print(110 in linked)
    print(linked)
    linked.reverse()
    print(linked)
    print(linked.peekHead())
    print(linked.peekLast())
    linked.add(1)
    print(linked)
    lst = linked.createAsList()
    print(lst)
    new = linked.copy()
    print("New: ", new)
    print(len(linked))
    print(linked.pop(3))
    print(linked)
    print(len(linked))
    linked.pop()
    print(linked)
    print(len(linked))
    print(linked.remove())
    print(linked, len(linked))
    print(linked.is_empty())
    print(linked.removeLast(), linked, len(linked))
    print(linked.removeLast(), linked, len(linked))
    print(new)
    print(len(new))
    linked.insert(20,0)
    linked.insert(30,66)
    print(linked, len(linked))
    linked.replace(2,10)
    print(linked)
    print(linked)
    print(linked[len(linked) - 1])
    print(new)
"""

