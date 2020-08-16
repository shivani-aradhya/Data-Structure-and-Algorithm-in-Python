class Solution:
    def climbstairs(self,n):
        if n <= 2:
            return n
        step = [0] * (n + 1)
        step[1] = 1
        step[2] = 2
        for i in range(3, n+1):
            step[i] = step[i-1] + step[i-2]
        return step[n]

result = Solution()
print("Ways to climb 5 stairs: ", result.climbstairs(5))
print("Ways to climb 4 stairs: ", result.climbstairs(4))
print("Ways to climb 3 stairs: ", result.climbstairs(3))
