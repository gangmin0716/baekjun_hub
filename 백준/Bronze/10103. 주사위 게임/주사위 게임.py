a = int(input())

c = 100
s = 100

for i in range(a):
    n, m = map(int, input().split())
    if n > m:
        s -= n
    elif n < m:
        c -= m
print(c)
print(s)