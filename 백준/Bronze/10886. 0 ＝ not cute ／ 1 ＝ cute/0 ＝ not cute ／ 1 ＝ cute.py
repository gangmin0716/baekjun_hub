a = int(input())
Y_cute = 0
N_cute = 0

for _ in range(a):
    user = int(input())
    if user == 1:
        Y_cute += 1
    elif user == 0:
        N_cute += 1


if Y_cute > N_cute:
    print("Junhee is cute!")
elif Y_cute < N_cute:
    print("Junhee is not cute!")