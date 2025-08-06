def fac(n):
    if n == 1:
        return 1
    else:
        return n + fac(n - 1)

## main
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(fac(n))