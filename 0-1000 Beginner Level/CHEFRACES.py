import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y,a,b = [int(x) for x in input().split()]
    count = 0
    if x not in [a,b]:
        count+=1
    if y not in [a,b]:
        count+=1
    print(count)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
