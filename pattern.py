'''1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 '''
for i in range(num):
        a = 1
        for j in range(i+1):
            print(a, end=' ')
            a+=1
        print(" ")

'''1  
2 1  
3 2 1  
4 3 2 1  
5 4 3 2 1  
for i in range(num):
        for j in range(i+1,0 ,-1):
            print(j, end=' ')
        print(" ")
        
5 4 3 2 1  
4 3 2 1  
3 2 1  
2 1  
1 
for i in range(0,5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print()
    
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()
    
1 
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1 
rows = 5
k = 2 * rows - 2
for i in range(1, rows+1):
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(i,0,-1):
        print(j, end=" ")
    print("")
    
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
rows = 5
current_Number = 1
stop =2
for i in range(rows):  
    for j in range(1, stop):  
        print(current_Number, end=' ')  
        current_Number += 1  
    print("")  
    stop += 1  
    
1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

rows = 5


for i in range(1, rows+1):
    numberOfSpaces = (rows-i)*2
    for j in range(numberOfSpaces):
        print(" ",end="")
    for x in range(1,i):
        print(x,end=" ")
    for x in range(i,0,-1):
        print(x,end=" ")
    print()
   
   
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
n=5
m=5
for i in range(1, n+1) :
    for j in range(1, m+1) :
        if (i == 1 or i == n or
            j == 1 or j == m) :
            print("*", end=" ")           
        else :
            print(" ", end=" ")           
         
    print()
