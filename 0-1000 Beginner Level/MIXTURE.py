import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b = [int(x) for x in input().split()]
    if a and b:
        print('Solution')
    elif a and not b:
        print('Solid')
    elif not a and b:
        print('Liquid')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
