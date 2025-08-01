a = int(input())
total_list = []
for i in range(a):
    total = 0
    di_1, di_2, di_3 = map(int, input().split())
    if di_1 == di_2 and di_3 == di_1:
        total += 10000 + (di_1 * 1000)
        total_list.append(total)

    elif di_1 == di_2 or di_1 == di_3:
        total += 1000 + (di_1 * 100)
        total_list.append(total)
    elif di_2 == di_3:
        total += 1000 + (di_2 * 100)
        total_list.append(total)

    else:
        if di_1 > di_2 and di_1 > di_3:
            total += (di_1 * 100)
        elif di_2 > di_3 and di_2 > di_1:
            total += (di_2 * 100)
        elif di_3 > di_1 and di_3 > di_2:
            total += (di_3 * 100)
        total_list.append(total)
total_list.sort()
print(total_list[-1])