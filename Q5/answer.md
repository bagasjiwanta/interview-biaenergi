# Question #5 (algorithm)

A Prime number is defined as a positive integer greater than 1 that is divisible only by 1 and itself. When the number is divided by any other positive integers, it would have remainders.

For example:

- 7 is a Prime number since it could be divided by 1 and 7 only.
- 9 is NOT a Prime number since it could be divided by 3.

QUESTION:

Please write a method to print out ALL the Prime numbers between 2 and 100.

```py
def print_primes_2_to_100():
    for candidate in range(2, 100 + 1):
        prime = True
        for j in range(2, int(math.sqrt(candidate)) + 1):
            if candidate % j == 0:
                prime = False
                break
        if prime:
            print(candidate, end=" ")
```

Loop from 2 to 100, then for every candidate, we check from if that number 2 to sqrt(candidate). This is to minimize the time of calculation because if the candidate is not divisible to any number up to its square root, then it's not divisable with the numbers after the square root.

For example let's take 24. The factors of 24 (sorted) are:

1 2 3 4 6 8 12 24

The square root of 24 is 4.899 or if we round to the upper integer, 5. 5 sits between the factors right after 4:

1 2 3 4 **5** 6 8 12 24

Now, every number on the left side needs to be multiplied with the right side to make 24. So, we only need to check the numbers in the left.
