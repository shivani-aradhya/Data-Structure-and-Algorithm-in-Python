#Testcasetaken as an arr[12,15,3,10,4]

def Insertion_sort(mylist):
    for i in range(1, len(mylist)):
        value= mylist[i]
        pos=i
        while value< mylist[pos-1] and pos>0:
            mylist[pos]= mylist[pos-1]
            pos= pos-1
        mylist[pos]= value


arr=[12,15,3,10,4]
Insertion_sort(arr)
print(arr)