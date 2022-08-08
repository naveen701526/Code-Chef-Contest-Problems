import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    s = input()
    val = s.count('4')
    print(val)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
