N, M = map(int,input().split())

baguni = [0]*N

for aa in range(M):
    i, j, k = map(int,input().split())
    for ii in range(i, j+1):
        baguni[ii - 1] = k

for i in baguni:
    print(i, end=" ")
