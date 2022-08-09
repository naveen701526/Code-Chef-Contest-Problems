import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    if n >= 2000:
        print(1)
    elif n >= 1600 and n <2000:
        print(2)
    else:
        print(3)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
