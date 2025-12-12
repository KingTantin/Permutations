import time
def prime_numbers(n, twin_primes=False):
    prime_numbers = []

    for number in range(2, n):
        if number % 1000 == 0:
            print(number)
        prime = True
        max_check = int(number**(1/2))
    
        for prime_num in prime_numbers:
            if number % prime_num == 0:
                prime = False
                break
            elif prime_num > max_check:
                break
        if prime == True:
            prime_numbers.append(number)

    if twin_primes == True:
        for i in range(len(prime_numbers)-1):
            if prime_numbers[i] + 2 == prime_numbers[i+1]:
                print(prime_numbers[i], prime_numbers[i+1])

    return prime_numbers








start = time.time()
n = 10000
x = prime_numbers(n)
end = time.time()

print(x)
print(n/len(x))
print(end-start)
