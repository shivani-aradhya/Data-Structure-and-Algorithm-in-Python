#Kadane algorithm
def maxarray(arr):
    totalmax= 0
    currentmax=0
    l = len(arr)
    startindex=0
    endindex=0
    s=0
    for i in range(0, l):
        currentmax= currentmax+ arr[i]
        if currentmax < 0:
           currentmax=0
           s= i+1
        else:
            if currentmax > totalmax:
                totalmax= currentmax
                startindex=s
                endindex=i

    print("Maximum contigous sum: ", totalmax)
    print ("Starting index and Ending index: " , startindex, 'and' , endindex)


a=[-1,-2.-3,6,4,2,-1]
a= maxarray(a)
