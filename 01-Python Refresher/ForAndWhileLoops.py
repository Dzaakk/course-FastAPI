my_list = [1, 2, 3, 4, 5]

for x in range(3, 6):
    print(x)

sum_loop = 0

for x in my_list:
    sum_loop += x

print(sum_loop)


people_list = ["Bob", "Eric", "Drake"]

for x in people_list:
    print(f"Hi {x}!")


i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")
