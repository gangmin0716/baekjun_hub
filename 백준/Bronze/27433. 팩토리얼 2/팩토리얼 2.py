def fac(a):
    if a == 0:
        return 1
    else:
        total = a * fac(a - 1)
    return total

## main

a = int(input())

print(fac(a))