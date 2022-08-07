import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b = [int(x) for x in input().split()]
    print(21-a-b if 21-a-b > 0 and 21-a-b in range(1,11) else -1 )
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
