n=int(input())
for i in range(n):
    data = input()
    for elem in data[ : : 2] :
        print(elem,end="")
    print(end=" ")
    for elem1 in data[ 1: : 2] :
        print(elem1,end="")
    
    print(" ")