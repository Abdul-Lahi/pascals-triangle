pascals_T = [[1]]
sequence = int(input('Enter number of sequence: '))
for x in range(1, sequence):
    if len(pascals_T) == 1:
        pascals_T.append([1,1])
    elif len(pascals_T) > 1:
        newlist = [1]
        for y in range(1, x):
            newlist.append(pascals_T[x-1][y-1] + pascals_T[x-1][y])
        newlist.append(1)
        pascals_T.append(newlist)

print(pascals_T).split()
