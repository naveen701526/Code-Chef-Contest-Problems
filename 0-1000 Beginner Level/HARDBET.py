import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    sa,sb,sc = [int(x) for x in input().split()]
    val = min(sa,sb,sc)
    if val == sa:
        print('Draw')
    elif val == sb:
        print('Bob')
    elif val == sc:
        print('Alice')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
