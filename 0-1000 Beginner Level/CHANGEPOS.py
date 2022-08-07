import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    sx,sy,ex,ey = [int(x) for x in input().split()]
    if sx == ex or sy == ey:
        print(2)
    else:
        print(1)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
