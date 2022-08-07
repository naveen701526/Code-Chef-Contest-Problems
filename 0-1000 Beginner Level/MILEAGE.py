import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n,x,y,a,b = [int(x) for x in input().split()]
    if (n*x)/a < (n*y)/b:
        print('PETROL')
    elif (n*x)/a > (n*y)/b:
        print('DIESEL')
    else:
        print('ANY')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
