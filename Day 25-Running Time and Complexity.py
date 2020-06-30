import math
        
def is_prime(number):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    x = 5
    while x*x <= n:
        if n % x == 0 or n % (x+2) ==0:
            return False
        x = x + 6
    return True

T = int(input())
for i in range(0,T):
    n=int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")