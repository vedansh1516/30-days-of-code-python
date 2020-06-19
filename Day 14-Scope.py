class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.maximumDifference= 0
        a.sort()
        l=len(a)
        c= abs(a[0]-a[l-1])
        self.maximumDifference=c
        

    # Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)