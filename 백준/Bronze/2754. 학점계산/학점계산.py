A = list(input())

if A[0] in "A":
    if A[1] in "+":
        print(4.3)
    elif A[1] in "0":
        print(4.0)
    elif A[1] in "-":
        print(3.7)

elif A[0] in "B":
    if A[1] in "+":
        print(3.3)
    elif A[1] in "0":
        print(3.0)
    elif A[1] in "-":
        print(2.7)

elif A[0] in "C":
    if A[1] in "+":
        print(2.3)
    elif A[1] in "0":
        print(2.0)
    elif A[1] in "-":
        print(1.7)

elif A[0] in "D":
    if A[1] in "+":
        print(1.3)
    elif A[1] in "0":
        print(1.0)
    elif A[1] in "-":
        print(0.7)
elif A[0] in "F":
    print(0.0)