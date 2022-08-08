import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    prime[1] = False
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    return prime

# credit geeks for geeks
# https://bit.ly/3bEKCrQ


prime = SieveOfEratosthenes(100000)


def answer_finder():
    n = int(input())
    if prime[n]:
        print('yes')
    else:
        print('no')


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
