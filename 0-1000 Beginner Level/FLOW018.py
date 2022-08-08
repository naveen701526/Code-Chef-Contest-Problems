import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')

def facts(n):
    if n <= 1:
        return 1
    return facts(n-1)*n

def answer_finder():
    n = int(input())
    print(facts(n))


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
