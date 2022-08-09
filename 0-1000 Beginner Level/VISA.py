import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x1,x2,y1,y2,z1,z2 = [int(x) for x in input().split()]
    condition_1 = x2 >= x1
    condition_2 = y2 >= y1
    condition_3 = z2 <= z1
    if condition_1 and condition_2 and condition_3:
        print('YES')
    else:
        print('NO')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
