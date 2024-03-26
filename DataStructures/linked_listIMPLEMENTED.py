# ----STEPS TO MAKE A LINKED LIST-----
#Create Node
#Create Linked List
#Add Nodes to LL

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,newNode):
        if self.head is None:
            self.head=newNode
            print("\n The Node has been Added\n")
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next=newNode
    
    def showlist(self):
        currentNode=self.head
        if currentNode is None:
            print("\nThe linked list is Empty\n")
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
    
    def insertAtBeginning(self,newNode):
        temp=self.head
        self.head = newNode
        self.head.next = temp
    
    def insertAtIndex(self,index,newNode):
        if index ==1:
            linkedList.insertAtBeginning(newNode)
        else:
            counter=1
            currentNode=self.head
            while True:
                if counter == index-1:
                    temp=currentNode.next
                    currentNode.next=newNode
                    newNode.next=temp
                    break
                elif currentNode.next is None:
                    print("\nThe index does not exist..\n")
                    break
                else:
                    counter+=1
                    currentNode=currentNode.next
    
    def deleteFromIndex(self,index):
        currentNode=self.head
        if index==1:
            self.head=currentNode.next
            return("Element deleted from the index ",index)
        else:
            counter=1
            while True:
                if counter==index-1:
                    temp=currentNode.next
                    currentNode.next=temp.next
                    break
                else:
                    counter+=1
                    currentNode=currentNode.next




# =========> USER INTERACTION PART STARTS FROM HERE <============
linkedList=LinkedList()           
option =float('inf')
while True:
    print("---What would you like to do---\n0.Exit\n1.Show Linked List \n2.Insert Node at End\n4.Insert Node at Head\n5.Insert At Specific Index\n6.Delete from certian Index\n-------------------------------")
    option=int(input("Enter your choice :"))
    if option ==0:
        exit()
    elif option ==1:
        linkedList.showlist()
    elif option ==2:
        newNode = Node(input("Enter the data of the Node :"))
        linkedList.insertAtEnd(newNode)
    elif option ==4:
        insertionAtHead = Node(input("Enter the data of the new Head Node : "))
        linkedList.insertAtBeginning(insertionAtHead)
    elif option ==5:
        print("Indexing starts from 1 , 1 being the Head")
        index=int(input("Enter the index where you want to add the Node :"))
        newNode = Node(input("enter the Data of the Node :"))
        linkedList.insertAtIndex(index,newNode)
    elif option ==6:
        index=int(input("enter the index of Node you want to Delete : "))
        linkedList.deleteFromIndex(index)
    else:
        print("Invalid Opiton Entered")
