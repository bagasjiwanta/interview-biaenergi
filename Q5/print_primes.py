import math


def print_primes_2_to_100():
    '''Print prime numbers from 2 to 100 with space separator'''
    for candidate in range(2, 100 + 1):
        prime = True
        for j in range(2, int(math.sqrt(candidate)) + 1):
            if candidate % j == 0:
                prime = False
                break
        if prime:
            print(candidate, end=" ")


if __name__ == '__main__':
    print_primes_2_to_100()
