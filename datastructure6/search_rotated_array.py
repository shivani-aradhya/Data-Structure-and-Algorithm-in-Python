class Solution:
    def searcharray(self, arr, target):
        start = 0
        end = len(arr)
        while start < end:
            mid = (start + end)//2
            if arr[mid] == target:
                return mid
            if arr[start] <= arr[mid]:
                if target >= arr[start] and target < arr[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if target <= arr[end] and target > arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

result = Solution()
arr = [4,5,6,7,0,1,2]
target = 0
print("Position of " +str(target)+ " in " + str(arr))
print(result.searcharray(arr, target))

target = 1
print("Position of " +str(target)+ " in " + str(arr))
print(result.searcharray(arr, target))

target = 10
print("Position of " +str(target)+ " in " + str(arr))
print(result.searcharray(arr, target))






