import sys
sys.setrecursionlimit(10000)
f = open("input.txt")
my_ls = []
for line in f:
    line = line.strip("\n")
    line = list(line)
    my_ls.append(line)
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
for i in range(len(my_ls)):
    for j in range(len(my_ls[0])):
        if my_ls[i][j] == "^":
            start = [i,j,0]
travelled = [start]
sol = [start[0:2]]
index = 0
def travel(i,j, index):
    if not (0 <= i + dirs[index][0] < len(my_ls)) or not (0 <= j + dirs[index][1] < len(my_ls)):
        return None
    elif my_ls[i+dirs[index][0]][j+dirs[index][1]] == "." or my_ls[i+dirs[index][0]][j+dirs[index][1]] == "^":
        if [i+dirs[index][0],j+dirs[index][1]] not in sol:
            travelled.append([i+dirs[index][0],j+dirs[index][1], index])
            sol.append([i+dirs[index][0],j+dirs[index][1]])
            travel(i+dirs[index][0],j+dirs[index][1], index)
        else:
            travel(i+dirs[index][0],j+dirs[index][1], index)
    elif my_ls[i+dirs[index][0]][j+dirs[index][1]] == "#":
        index = (index+1)%4
        travel(i,j,index)
travel(start[0],start[1],index)
print(len(travelled))
