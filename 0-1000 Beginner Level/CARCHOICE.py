import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x1,x2,y1,y2 = [int(x) for x in input().split()]
    val1 = x1/y1
    val2 = x2/y2
    if val1 > val2:
        print(-1)
    elif val1 < val2:
        print(1)
    elif val1 == val2:
        print(0)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
