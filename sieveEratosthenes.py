"""
Sieve of Eratosthenes -
is one of the most efficient ways to find all of the smaller primes
"""
import math

def sieveEratosthenes(in_value):
    temp_list = [True] * (in_value + 1) # initialize to True
    temp_list[0] = False
    temp_list[1] = False

    for i in range( int(math.sqrt(in_value)) +1):
        if temp_list[i]:
            for j in range(i*i, in_value + 1, i):
                temp_list[j] = False
                
    prime_list = []
    for i in range(in_value + 1):
        if temp_list[i] == True:
            prime_list.append(i)
    return prime_list

def main():
    try:
        n = int(input('Enter an interge ( number >1): '))
    except ValueError:
        print ('Enter an integer ( number> 1): ')
        main()
    if n < 1:
            main()
    print (sieveEratosthenes(n))
    
if __name__ == '__main__':
    main()
