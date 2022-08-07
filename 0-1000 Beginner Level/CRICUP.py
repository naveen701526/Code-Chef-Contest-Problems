import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y,d = [int(x) for x in input().split()]
    if abs(x-y) <= d:
        print('YES')
    else:
        print('NO')


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
