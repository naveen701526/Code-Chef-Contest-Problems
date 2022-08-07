import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    p = int(input())
    count = 0
    while p >= 100:
        p -= 100
        count+=1
    while p >= 1:
        p-=1
        count+=1
    if count <= 10:
        print(count)
    else:
        print(-1)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
