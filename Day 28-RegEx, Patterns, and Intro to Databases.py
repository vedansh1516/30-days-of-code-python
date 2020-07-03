import sys, re

names = []
pattern=re.compile('@gmail.com$')

N = int(input().strip())
for i in range(N):
    firstName,emailID=input().strip().split(' ')
    if pattern.search(emailID):
        names.append(firstName)
names.sort()
for name in names:
    print(name)