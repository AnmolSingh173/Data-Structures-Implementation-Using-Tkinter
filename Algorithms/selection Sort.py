# Implemented Selection Sort 

arr=[12,23,4,5,7,45]
def selectionSort(arr):
    i,j=0,1
    while i!=len(arr)-1:
        if j==len(arr)-1:
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp           
            i+=1
            j=i+1
        elif arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1
        else:
            j+=1
    return arr

print(selectionSort(arr))

