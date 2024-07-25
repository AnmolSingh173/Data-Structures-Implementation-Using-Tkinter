from collections import defaultdict
hmap = defaultdict(list)

def insert(key, value):
    hmap[key].append(value)

def delete(key):
    if key in hmap:
        del hmap[key]
    else:
        print("The key does not exist in the HashMap")

def display():
    result = list(hmap.items())
    print(result)

def check(key):
    if key in hmap:
        hmap[key].items()
    else:
        print("The key does not exists in the HashMap")

n = float('inf')
while n != 0:
    print("\n What would you like to do ? \n 1.Show Key-Value pairs \n 2.Insert Items into HashMap \n 3.Check if Items exists in HashMap \n 4.Delete a Key ")
    n = int(input("Enter your choice : "))
    if n == 4:
        break

    elif n == 1:
        display()

    elif n == 2:
        key = (input("Enter the key : "))
        value = input("Enter the value to be added : ")
        insert(key, value)
    
    elif n == 3:
        key = input("Enter the Key : ")
        check(key)
    
    elif n==4 : 
        key=input("Enter the Key to be removed ")
        delete(key)
    else:
        print("Invalid option entered")
