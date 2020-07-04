import heapq
lst1= [7, 10 ,2,4,1,5,25,11,12]
lst2= [27,83,12,23,64,75,89,67,54]

heapq.heapify(lst1)
heapq.heapify(lst2)
print("First Heap is:",list(lst1))
print("Second Heap is:",list(lst2))

heapq.heappush(lst1 , 14)
heapq.heappush(lst2 , 14)
heapq.heappop(lst1)
heapq.heappop(lst2)

print("Modified Heap is:",list(lst1))
print("Modified Heap is:",list(lst2) , '\n')

print("The three largest elements of first heap are: ", heapq.nlargest(3,lst1))
print("The three smallest elements of first heap are: ", heapq.nsmallest(3,lst1) , '\n')

print("The three largest elements of second heap are: ", heapq.nlargest(3,lst2))
print("The three smallest elements of second heap are: ", heapq.nsmallest(3,lst2))