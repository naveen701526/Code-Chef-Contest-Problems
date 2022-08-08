import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b,c = [int(x) for x in input().split()]
    print('YES' if a+b+c == 180 else 'NO')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
