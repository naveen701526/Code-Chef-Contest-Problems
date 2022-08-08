import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n % 2:
        print(-1)
    else:
        val = arr.count(1)
        val1 = arr.count(-1)
        val = abs((n//2) - val)
        val1 = abs((n//2)-val1)
        print(min(val,val1))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
