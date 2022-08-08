import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y,z = [int(x) for x in input().split()]
    val = y - x
    if val <= 0:
        print('YES')
    else:
        val1 = z*2
        if val1 + x >= y:
            print('YES')
        else:
            print('NO')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
