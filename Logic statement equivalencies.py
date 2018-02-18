# This small script allows you to compare a reference statement with a group of
# alternatives. The program will print the alternatives that are equivalent to
# that reference statement.

ref = '(not(c[0]) and c[1]) or (c[1] and (not(c[1]) or not(c[1])))'

# create permutations of booleans [[True, True, False], [True, False, False], ...]
bools = [True, False]
cases = [(i, j, k) for i in bools for j in bools for k in bools]

# alternatives/options
alts = [['a', 'c[1] and not(c[0]) and not(c[1])'],
        ['b', 'c[1] and not(c[0] or c[1])'],
        ['c', 'not(not(c[1]) or (not(c[0]) and not(c[1])))'],
        ['d', 'not(not(c[1]) or (c[0] and c[1]))']]

# contains all possibles answers that will be discarded later
eq_ans = [a[0] for a in alts]

# iterate over alternatives
for i in range(len(alts)):
    # iterate over cases
    for c in cases:
        # if alternative is not equal to reference, remove alternative from 'correct_ans'
        if eval(alts[i][1]) != eval(ref):
            eq_ans.remove(alts[i][0])
            break

print("Equivalent answers:", eq_ans)
