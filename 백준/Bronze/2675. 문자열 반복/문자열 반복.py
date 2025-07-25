S = int(input())

for i in range(S):
    a, b = input().split()
    a = int(a)
    for i in b:
        print(i * a, end='')
    print()