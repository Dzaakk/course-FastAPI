my_list = [80, 10, 90, 8, 7]
print(my_list)
print(my_list[1])

people_list = ["Bob", "Eric", "Drake"]
print(people_list)
print(people_list[-1])
people_list[0] = "Mel"
print(people_list[0])

print(len(people_list))

print(my_list[0:2])
print(my_list[1:4])

my_list.append(1000)
print(my_list)

my_list.insert(1, 2000)
print(my_list)

my_list.remove(1000)
print(my_list)

my_list.pop(0)
print(my_list)

my_list.sort()
print(my_list)
