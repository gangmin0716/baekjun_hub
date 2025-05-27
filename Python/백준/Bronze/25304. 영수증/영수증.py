money = int(input())
n = int(input())
result = 0

for i in range(n):
	s, ss = map(int,input().split())
	result += (s * ss)

if money == result:
	print("Yes")
else:
	print("No")
