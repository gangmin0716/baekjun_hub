num_list = []

for _ in range(5):
    jumsu = int(input())
    if jumsu < 40:
        jumsu = 40
        num_list.append(jumsu)
    else:
        num_list.append(jumsu)

print(f'{sum(num_list) / len(num_list):.0f}')