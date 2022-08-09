import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y,z = [int(x) for x in input().split()]
    if x + y == z:
        print('EQUAL')
        return 
    val = min(x+y,z)
    if val == z:
        print('TRAIN')
    else:
        print('PLANEBUS')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
