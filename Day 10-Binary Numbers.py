n=int(input())
a=list(bin(n)[2:])
count=0
max_count=0
for i in a:
    if(i=="1"):
        count=count+1
    else:
        if(count>max_count):
            max_count=count
        count=0
if count > max_count:
    max_count = count
print (max_count)