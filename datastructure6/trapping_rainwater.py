class Solution:
    def trapwater(self, arr):
        l= len(arr)
        maxwater = 0
        for i in range(1, l-1):
            left = arr[i]
            for j in range(i):
                left = max(arr[j], left)

            right = arr[i]
            for j in range(i+1, l):
                right = max(arr[j], right)

            maxwater = maxwater + (min(left, right) - arr[i])

        return maxwater

output = Solution()
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(output.trapwater(arr))



