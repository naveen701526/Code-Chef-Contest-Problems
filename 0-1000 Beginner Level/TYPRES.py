import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    print('NO' if not n%4 else 'YES')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
