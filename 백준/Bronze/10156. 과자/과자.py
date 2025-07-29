a, b, c = map(int, input().split())
hap = a * b

if hap - c > 0:
    print(hap - c)
else:
    print(0)