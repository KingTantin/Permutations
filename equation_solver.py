import time
def perm_generater(max_perm, num_perm, current_perm):
    results = []
    if num_perm == 1:
        results.append(current_perm.copy())
        return results #unneeded in this case 
    switch = max_perm-num_perm
    for i in range(switch, max_perm):
        current_perm[switch], current_perm[i] = current_perm[i], current_perm[switch]
        results.extend(perm_generater(max_perm, num_perm-1, current_perm))
        current_perm[switch], current_perm[i] = current_perm[i], current_perm[switch]
    return results

start = time.time()
n = 9
permutation_n = perm_generater(n, n, list(range(1,n+1)))

counter = 0
for i in range(len(permutation_n)):
    if 76 == permutation_n[i][0]+13*permutation_n[i][1]/permutation_n[i][2]+permutation_n[i][3]+12*permutation_n[i][4]-permutation_n[i][5]-11+permutation_n[i][6]*permutation_n[i][7]/permutation_n[i][8]:
        counter += 1
        print(permutation_n[i][0], permutation_n[i][1], permutation_n[i][2], permutation_n[i][3], permutation_n[i][4], permutation_n[i][5], permutation_n[i][6], permutation_n[i][7], permutation_n[i][8])
print(counter)

end = time.time()
print(end-start)


#import itertools

#counter = 0
#for perm in itertools.permutations(range(1,10)):
#    if 76 == perm[0]+13*perm[1]/perm[2]+perm[3]+12*perm[4]-perm[5]-11+perm[6]*perm[7]/perm[8]:
#        counter += 1
#        print(perm[0], perm[1], perm[2], perm[3], perm[4], perm[5], perm[6], perm[7], perm[8])
#print(counter)
