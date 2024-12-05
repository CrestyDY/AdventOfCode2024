w = open("input.txt")
my_list = []
for line in w:
    line = line.strip("\n")
    line = line.split(" ")
    line = [int(x) for x in line]
    my_list.append(line)
'''sol = 0
for i in range(len(my_list)):
    valid = True
    p1 = 0
    p2 = 1
    while my_list[i][p1] == my_list[i][p2]:
        p1 += 1
        p2 += 1
    if my_list[i][p1] > my_list[i][p2]:
        decreasing = True
    else:
        decreasing = False
    for j in range(len(my_list[i])-1):
        if decreasing:
            if my_list[i][j] < my_list[i][j+1] or not (1<=abs(my_list[i][j]-my_list[i][j+1])<=3):
                valid = False
                break
        elif not decreasing:
            if my_list[i][j] > my_list[i][j+1] or not (1<=abs(my_list[i][j]-my_list[i][j+1])<=3):
                valid = False
                break
    if valid:
        sol += 1
print(sol)'''

def is_safe(ls):
    """Checks if a sequence is safe according to the rules."""
    if len(ls) < 2:
        return True

    # Determine if the sequence is increasing or decreasing
    p1, p2 = 0, 1
    while p2 < len(ls) and ls[p1] == ls[p2]:
        p1 += 1
        p2 += 1
    if p2 == len(ls):
        return True

    decreasing = ls[p1] > ls[p2]

    # Validate the sequence based on the trend
    for j in range(len(ls) - 1):
        diff = abs(ls[j] - ls[j + 1])
        if (decreasing and (ls[j] < ls[j + 1] or not (1 <= diff <= 3))) or \
           (not decreasing and (ls[j] > ls[j + 1] or not (1 <= diff <= 3))):
            return False
    return True

safe_reports = 0

for sublist in my_list:
    if is_safe(sublist):
        # Sequence is already safe
        safe_reports += 1
        continue

    # Check if removing one level can make the sequence safe
    dampened_safe = False
    for j in range(len(sublist)):
        modified_sublist = sublist[:j] + sublist[j + 1:]
        if is_safe(modified_sublist):
            dampened_safe = True
            break
    if dampened_safe:
        safe_reports += 1
print(safe_reports)

