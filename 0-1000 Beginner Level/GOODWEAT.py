import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    arr = [int(x) for x in input().split()]
    val1 = arr.count(1)
    val2 = arr.count(0)
    if val1 > val2:
        print('YES')
    else:
        print('NO')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
