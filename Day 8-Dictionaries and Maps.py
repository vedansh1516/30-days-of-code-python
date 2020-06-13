n=int(input())
d={}
for i in range(n):
    command= input().split()
    d[command[0]] = command[1]
try:
    while True:
        query= input()
        if query in d:
            print(query+"="+d.get(query))
        else:
            print("Not found")
except EOFError:
    pass
    




