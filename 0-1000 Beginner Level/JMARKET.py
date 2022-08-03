# import sys
# sys.stdout = open('./output.txt', 'w')
# sys.stdin = open('./input.txt', 'r')


def answer_finder():
    #n = int(input())
    x,a,b,c = [int(x) for x in input().split()]
    val = min(a,b,c) * (x-1)
    if min(a,b,c) == a:
        print(val+min(b,c))
    elif min(a,b,c) == b:
        print(val+min(a,c))
    else:
        print(val+min(a,b))



test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
