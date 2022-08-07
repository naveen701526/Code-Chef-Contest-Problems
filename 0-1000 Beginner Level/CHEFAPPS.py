import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    #n = int(input())
    s,x,y,z = [int(x) for x in input().split()]
    val = s - x - y
    if z <= val:
        print(0)
    elif z <= val + max(x,y):
        print(1)
    else:
        print(2)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
