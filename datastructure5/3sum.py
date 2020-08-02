def threesum(arr):
    result = []
    l = len(arr)
    exist = False
    arr.sort()
    for i in range(0, l-1):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1
        right = l - 1
        temp = arr[i]

        while(left < right):
            s = temp + arr[left] + arr[right]
            if(s < 0):
                left += 1
            elif(s >0):
                right -= 1
            else:
                result.append((temp, arr[left], arr[right]))
                exist = True
                while ( left < right and arr[left]== arr[left + 1]):
                    left += 1
                while (left < right and arr[right] == arr[right - 1]):
                    right -= 1

                left += 1
                right -= 1

    if exist == False:
        print("THREE SUM TRIPLET DOES NOT EXIST")
    return result



arr1= [-1, 0, 1, 2, -1, -4]
print("ARRAY:", arr1)
print("THREE SUM TRIPLETS", threesum(arr1))
arr2 =[1, 2, 3, 4, 5]
print("ARRAY:", arr2)
threesum(arr2)









