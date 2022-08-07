import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b,c,d = [int(x) for x in input().split()]
    if a+c==180 and b+d==180:
        print('YES')
    else:
        print('NO')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
