def isPrime(num):
    if num < 2:
        return False
    else:
        i = 2
        while i < num:
            print(num % i)
            if (num % i) != 0:
                i += 1
            else:
                return False
        return True

def mySqrt(x):
    notClose = True
    y = (x + 1)/2
    while notClose:
        if  x - y ** 2 < 0.001 and x - y ** 2 > -0.001:
            notClose = False
            return y
        print(y)
        y = (y + x/y)/2

print(mySqrt(24))