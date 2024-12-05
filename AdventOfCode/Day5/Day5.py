f = open("input.txt")
pairs = True
pairs_ls = []
update_ls = []
for line in f:
    if line == "\n":
        pairs = False
        continue
    if pairs:
        line = line.strip("\n")
        line = line.split("|")
        line = [int(x) for x in line]
        pairs_ls.append(line)
    if not pairs:
        line = line.strip("\n")
        line = line.split(",")
        line = [int(x) for x in line]
        update_ls.append(line)
'''sol = []
for i in range(len(update_ls)):
    for j in range(len(update_ls[i])):
        bound  = len(update_ls[i])-j
        inc = 1
        while inc < bound:
            if [update_ls[i][j],update_ls[i][j+inc]] in pairs_ls:
                inc += 1
            else:
                break
        if inc != bound:
            break
    if inc == bound:
        sol.append(update_ls[i][len(update_ls[i])//2])
print(sum(sol))'''
#Part 2
faulty_updates = []
for i in range(len(update_ls)):
    for j in range(len(update_ls[i])):
        bound  = len(update_ls[i])-j
        inc = 1
        while inc < bound:
            if [update_ls[i][j],update_ls[i][j+inc]] in pairs_ls:
                inc += 1
            else:
                break
        if inc != bound:
            break
    if inc != bound:
        faulty_updates.append(update_ls[i])
sol = []
for i in range(len(faulty_updates)):
    counts = {}
    for j in range(len(faulty_updates[i])):
        count = 0
        bound  = len(faulty_updates[i])
        inc = 0
        while inc < bound:
            if [faulty_updates[i][j],faulty_updates[i][inc]] in pairs_ls:
                count += 1
                inc += 1
            else:
                inc += 1
        counts[faulty_updates[i][j]] = count
    counts = dict(sorted(counts.items(), key=lambda item: item[1]))
    sol.append(list(counts.keys())[len(counts.keys())//2])
print(sum(sol))
    
