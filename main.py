# import data

with open("Data.txt") as file:
    Input = [i for i in file.read().splitlines()]

    print(Input)

total = []
current = []

for entry in Input:
    if not entry:
        total.append(current)
        current = []
        continue

    current.append(entry)

print(total)
