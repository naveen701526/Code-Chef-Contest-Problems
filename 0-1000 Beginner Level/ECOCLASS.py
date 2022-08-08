import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    s = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        if s[i]==d[i]:
            count+=1
    print(count)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
