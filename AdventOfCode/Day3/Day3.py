f = open("input.txt")
my_ls = []
for line in f:
    line = line.strip("\n")
    my_ls.append(line)
#Part 1
sol = 0
for i in range(len(my_ls)):
    my_str = my_ls[i]
    left = 0
    right = 4
    while right < len(my_str):
        while my_str[left:right] != "mul(" and right < len(my_str):
            left += 1
            right += 1
        if right == len(my_str):
            break
        third = right
        while my_str[third] != ")" and (my_str[third].isdigit() or my_str[third] == ",") and third < len(my_str):
            third += 1
        if third == len(my_str):
            break
        elif my_str[third] == ")":
            new_ls = my_str[right:third].split(",")
            sol += int(new_ls[0])*int(new_ls[1])
            left += 1
            right += 1
        else:
            left += 1
            right += 1
print(sol)
#Part 2
sol = 0
do = True
for i in range(len(my_ls)):
    my_str = my_ls[i]
    left = 0
    right = 4
    while right < len(my_str):
        while my_str[left:right] != "mul(" and right < len(my_str):
            if my_str[left:right] == "do()":
                do = True
                left += 1
                right += 1
                continue
            if my_str[left:right] == "don'" and right < len(my_str)-3 and my_str[left:right+3] == "don't()":
                do = False
                left += 1
                right += 1
                continue
            else:
                left += 1
                right += 1
        if right == len(my_str):
            break
        third = right
        while my_str[third] != ")" and (my_str[third].isdigit() or my_str[third] == ",") and third < len(my_str):
            third += 1
        if third == len(my_str):
            break
        elif my_str[third] == ")":
            if not do:
                left += 1
                right += 1
                continue
            else:
                new_ls = my_str[right:third].split(",")
                sol += int(new_ls[0])*int(new_ls[1])
                left += 1
                right += 1
        else:
            left += 1
            right += 1
print(sol)
