import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    arr = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        if arr[i] in range(10, 61):
            count+=1
    print(count)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
