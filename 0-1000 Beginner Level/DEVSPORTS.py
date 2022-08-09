import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    z,y,a,b,c = [int(x) for x in input().split()]
    val = z - y
    if val >= (a+b+c):
        print('YES')
    else:
        print('NO')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
