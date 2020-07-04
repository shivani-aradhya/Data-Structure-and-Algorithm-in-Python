import array as arr
a= arr.array("i", [1, 2, 3])
print("Array:")
for i in range(0,3):
    print( a[i])
insert= input("Want to insert Y or N?")
if insert=="Y" or insert=="y":
    pos=int(input("Enter position"))
    element= int(input("Enter number to be inserted"))
    print(pos, element)
    a.insert(pos,element)
else:
    print("Exit")
print("New array:")
for i in range(len(a)):
    print(a[i])



