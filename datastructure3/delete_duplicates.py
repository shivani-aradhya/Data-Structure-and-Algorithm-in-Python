#Delete duplicates from a sorted array
def deleteduplicates(arr):
    l= len(arr)
    if l==0 or l==1:
        return arr
    j=0
    for i in range(0, l-1):
        if arr[i]!= arr[i+1]:
            arr[j]= arr[i]
            j=j+1
    arr[j]= arr[l-1]
    j = j+1
    arr= arr[:j]
    return arr

a= [0,0,0,0,1,1,1,2,3,3,4,4,5,5,5,6,6,7,7,8]
print("Original array:", a)
n= deleteduplicates(a)
print("New array: ", n)

