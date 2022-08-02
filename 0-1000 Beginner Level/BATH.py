import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    #n = int(input())
    arr = [int(x) for x in input().split()]
    y = 2*arr[1]
    x = arr[0]
    print(x//y)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
