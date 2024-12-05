w = open("input.txt")
my_list = []
for line in w:
    line = line.strip("\n")
    line = line.split("   ")
    my_list.append(line)
#Part 1
left_list = []
for i in range(len(my_list)):
    left_list.append(int(my_list[i][0]))
right_list = []
for j in range(len(my_list)):
    right_list.append(int(my_list[j][-1]))
left_list.sort()
right_list.sort()
my_sum = 0
for k in range(len(left_list)):
    sum += abs(left_list[k]-right_list[k])
print(my_sum)

#Part 2
left_list = []
for i in range(len(my_list)):
    left_list.append(int(my_list[i][0]))
right_list = []
for j in range(len(my_list)):
    right_list.append(int(my_list[j][-1]))
my_sum = 0
for k in range(len(left_list)):
    my_sum += left_list[k]*right_list.count(left_list[k])
print(my_sum)
