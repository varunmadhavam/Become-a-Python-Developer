def gcd(a,b):
    if b > a:
        return gcd(b,a)
    elif b <= 0:
        return a
    elif a%b == 0:
        return b
    else:
        return gcd(b,a%b)
print(gcd(2740,1760))