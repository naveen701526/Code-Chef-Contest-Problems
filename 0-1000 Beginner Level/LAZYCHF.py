import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,m,d = [int(x) for x in input().split()]
    print(min(x*m, x+d))
    
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
