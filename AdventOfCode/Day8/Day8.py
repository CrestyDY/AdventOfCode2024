f = open("input.txt")
my_grid = []
for line in f:
    line = line.strip("\n")
    line = list(line)
    my_grid.append(line)
symbols = {}
for i in range(len(my_grid)):
    for j in range(len(my_grid[i])):
        if my_grid[i][j] not in symbols.keys() and my_grid[i][j] != ".":
            symbols[my_grid[i][j]] = [[i,j]]
        elif my_grid[i][j] != ".":
            symbols[my_grid[i][j]].append([i,j])
def is_valid(pos1,pos2):
    if 0 <= pos1 < len(my_grid[0]) and 0<= pos2 < len(my_grid):
        return True
    else:
        return False
symbols_ls = list(symbols.keys())
part1 = {}
part2 = {}
for i in symbols_ls:
    my_ls = symbols.get(i)
    for j in range(len(my_ls)):
        index1, index2 = my_ls[j]
        part2[(index1,index2)] = None
        for k in range(j + 1, len(my_ls)):
            index3, index4 = my_ls[k]
            pos1, pos2 = (2*index1-index3, 2*index2-index4)
            if is_valid(pos1,pos2):
                part1[(pos1,pos2)] = None
            while is_valid(pos1,pos2):
                part2[(pos1,pos2)] = None
                pos1 = pos1-index3+index1
                pos2 = pos2-index4+index2
            pos3, pos4 = (2*index3-index1, 2*index4-index2)
            if is_valid(pos3,pos4):
                part1[(pos3,pos4)] = None
            while is_valid(pos3,pos4):
                part2[(pos3,pos4)] = None
                pos3 = pos3-index1+index3
                pos4 = pos4-index2+index4
print(len(list(part1.keys())))
print(len(list(part2.keys())))
