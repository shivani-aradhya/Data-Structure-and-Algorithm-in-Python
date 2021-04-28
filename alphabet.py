'''
A
AB
ABC
ABCD
ABCDE

'''
for i in range(65, 70):
    # inner loop for jth columns
    for j in range(65, i + 1):
        print(chr(j), end="")

    print()

ABCDE
ABCD
ABC
AB
A
for i in range(70, 65, -1):
    # inner loop for jth columns
    for j in range(65, i):
        print(chr(j), end="")

    print()



A
BC
CDE
DEFG
EFGHI
# Outer loop
for i in range(65,70):
    k=i
    # Inner loop
    for j in range(65,i+1):
        print(chr(k),end="")
        k=k+1
    print()

A
BA
CBA
DCBA
EDCBA
# Outer loop
for i in range(65,70):
    # Inner loop
    for j in range(i,64,-1):
        print(chr(j),end="")
    print()