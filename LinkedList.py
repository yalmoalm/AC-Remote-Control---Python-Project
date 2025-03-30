class Node:

    def __init__(self, data):

        self.value = data
        self.next = None
        print('New Node added.')
     

class LinkedList:


    def __init__(self):

        self.head = None
        self.SizeOfLinkedList = 0 
        self.InsertAtBegin()     


    def GetSizeOfLinkedList(self):
        print(self.SizeOfLinkedList)


    def PrintAllTheLinkedList(self):

        TempNode = self.head

        while TempNode is not None:
            print(TempNode.value)
            TempNode = TempNode.next

        raise IndexError('Finish the process.')

    def InsertAtBegin(self): #Insert Node to the head of the LinkedList.

        Mods = ['Fan', 'Auto', 'Cool', 'Dry', 'Heat']

        for mode in Mods:

            NewNode = Node(mode) #Instance of Node Class

            if self.head is None:
                self.head = NewNode
                NewNode.next = self.head
                
                

            TempNode = self.head
            while TempNode.next is not self.head:
                TempNode = TempNode.next

            TempNode.next = NewNode
            NewNode.next = self.head
            self.SizeOfLinkedList += 1

    def SearchForSpecificNode(self, location):

        TempNode = self.head

        for i in range(1, location):

            TempNode = TempNode.next

        return TempNode.value


def main():


    LinkedList1 = LinkedList()
    print(LinkedList1.SearchForSpecificNode(5))
  


if __name__ == '__main__':
    main()        


