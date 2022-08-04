import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    arr = list(input())
    for a in arr:
        if a == 'A':
            print('T', end="")
        elif a == 'T':
            print('A', end="")
        elif a == "C":
            print('G', end="")
        elif a == 'G':
            print('C', end="")
    print()


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
