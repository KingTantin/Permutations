import random
import numpy as np
def miller_rabin(n, iterations):
    if n in {2, 3}:
        return n, True, f'{(1-4**-iterations)*100} %'
    for iteration in range(iterations):
        k = random.randint(2, n-2)
        
        a = (n-1)
        seq = []
        while True:
            seq.append(pow(k,a, n))
            if a % 2 == 0 and a != 0:
                a //= 2
            else:
                break
        if validad_seq(seq, n) == False:
            return n, False, '100 %'
    return n, True, f'{(1-4**-iterations)*100} %'

def validad_seq(seq, n):
    for num in seq:
        if num == 1:
            continue
        elif num == n-1 and len(seq)>1:
            return True
        else:
            return False
    return True


n = 4169
is_prime = False
test_num = 10**n+2
while is_prime == False:
    prime, is_prime, percentage = miller_rabin(test_num, 10)
    print(f'1e+{n} {test_num-10**n}/{n*int(np.log(float(10)))} {is_prime} {percentage}')
    test_num += 1
        
#1e+3000 1027 largest Prime I found