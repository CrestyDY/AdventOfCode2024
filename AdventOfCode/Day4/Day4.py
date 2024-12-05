f = open("input.txt")
my_ls = []
for line in f:
    line = line.strip("\n")
    ls = list(line)
    my_ls.append(ls)
#Part 1
"""sol = []
directions = [(0,3,0,2,0,1),(3,0,2,0,1,0),(3,3,2,2,1,1),(3,-3,2,-2,1,-1)]
for i in range(len(my_ls)):
    for j in range(len(my_ls[0])):
        if my_ls[i][j] == "X" or my_ls[i][j] == "S":
            for k in directions:
                if i + k[0] < len(my_ls[0]) and 0 <= j + k[1] < len(my_ls):
                    my_string = my_ls[i][j]+my_ls[i+k[4]][j+k[5]]+my_ls[i+k[2]][j+k[3]]+my_ls[i+k[0]][j+k[1]]
                    if my_string == "XMAS" or my_string == "SAMX":
                        if [i,j,i+k[0],j+k[1]] not in sol:
                            sol.append([i,j,i+k[0],j+k[1]])
print(len(sol))"""

#Part 2
sol = 0
for i in range(0,len(my_ls)-2):
    for j in range(0,len(my_ls[0])-2):
        my_string1 = my_ls[i][j] + my_ls[i+1][j+1] + my_ls[i+2][j+2]
        my_string2 = my_ls[i+2][j] + my_ls[i+1][j+1] + my_ls[i][j+2]
        if (my_string1 == "MAS" or my_string1 == "SAM") and (my_string2 == "MAS" or my_string2 == "SAM"):
            sol += 1
print(sol)
                
                
