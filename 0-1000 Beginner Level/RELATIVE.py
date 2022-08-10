
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    g, c = [int(x) for x in input().split()]
    numerator = pow(c, 2)
    denominator = 2*g
    print(numerator//denominator)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
