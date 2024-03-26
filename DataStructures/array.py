option =float('inf')
arr=[]

def printArray():
    if len(arr)==0:
        print ("\nThe Array is Empty..\n")
    else:
        for i in arr:
            print(i)
def insert(value):
    arr.append(value)

def remElemet(value):
    if value not in arr:
        print("Element is not present in the Array")
    else:
        arr.remove(value)


while True:
    print("---What would you like to do---\n0.Exit\n1.Show Array \n2.Insert Element in the Array \n3.Remove Element from Array\n-------------------------------")
    option=int(input("Enter your choice :"))
    if option ==0:
        exit()
    elif option ==1:
        printArray()
    elif option ==2:
        value=(input("Enter the value to be added in the Array "))
        insert(value)
    elif option ==3:
        value=input("Enter the element you want to remmove from the Array :")
        remElemet(value)
    else:
        print("Invalid Opiton Entered")
