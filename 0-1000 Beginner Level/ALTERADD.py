import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b = [int(x) for x in input().split()]
    d = b - a
    if d%3==0 or d%3 == 1:
        print('YES')
    else:
        print('NO')

    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
