import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b = [int(x) for x in input().split()]
    if a + b<3:
        print(1)
    elif a+b in range(3, 11):
        print(2)
    elif a + b in range(11, 61):
        print(3)
    else:
        print(4)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
