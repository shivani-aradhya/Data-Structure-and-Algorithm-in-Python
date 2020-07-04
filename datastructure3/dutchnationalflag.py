#An array sorts itself based on the element of index i given by user.
def sort(arr, index):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid<=high:

        if arr[index]> arr[mid]:
            key = arr[mid]
            arr[mid] = arr[low]
            arr[low] = key
            mid = mid + 1
            low = low + 1
        elif arr[index]< arr[mid]:
            key = arr[mid]
            arr[mid] = arr[high]
            arr[high]= key
            high = high -1
        else:
            mid = mid +1
    return arr


def printarray(arr):
    for i in arr:
        print(i)

arr = [7,8,2,4,5,1,4,8,9,1,19,27,0]
print("Array before sorting:", arr)
arr = sort(arr, 2)
print("Array after sorting: ",arr)
arr1= [0,1,0,1,1,2,2,2,0,1]
print("Array before sorting:", arr1)
arr1= sort(arr1, 3)
print("Array after sorting:", arr1)




