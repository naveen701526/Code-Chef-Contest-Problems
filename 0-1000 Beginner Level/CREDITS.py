import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    if n > 65:
        print('Overload')
    elif n >= 35 and n <=65:
        print('Normal')
    else:
        print('Underload')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
