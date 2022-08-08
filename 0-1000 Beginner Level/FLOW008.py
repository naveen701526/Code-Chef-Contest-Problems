import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    if n < 10:
        print('Thanks for helping Chef!')
    else:
        print('-1')


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
