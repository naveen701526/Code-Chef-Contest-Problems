import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    #n = int(input())
    x1,y1,x2,y2 = [int(x) for x in input().split()]
    print(max(abs(x1-x2), abs(y1-y2)))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
