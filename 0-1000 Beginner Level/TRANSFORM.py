# import sys
# sys.stdout = open('./output.txt', 'w')
# sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    if (n + 1) % 3 == 0:
        print('SMALL')
    elif (n+1)%3 == 1:
        print('NORMAL')
    elif (n+1) % 3 == 2:
        print('HUGE')


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
