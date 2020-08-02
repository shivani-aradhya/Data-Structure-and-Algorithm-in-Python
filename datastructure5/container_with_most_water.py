#Container with most water

def maxwater(arr):
    l = len(arr)
    first = 0
    last = l-1
    maxarea = 0
    while first < last:
        area = min(arr[first], arr[last]) * (arr[last] - arr[first])
        maxarea = max(maxarea , area)

        if arr[first] < arr[last]:
            first +=1
        else:
            last-=1
    return maxarea

arr1= [1,2,3,4,5]
print("ARRAY:", arr1)
print("Container with max area will be:")
print(maxwater(arr1))

arr2= [6,7,8,9,10]
print("ARRAY:", arr2)
print("Container with max area will be:")
print(maxwater(arr2))
arr= []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    arr.append(ele)
print("Container with max area will be:")
print(maxwater(arr))