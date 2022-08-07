import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x = int(input())
    if x%10 != 0 and x % 5 != 0:
        print(-1)
    else:
        count = 0
        
        while x >= 10:
            x-=10
            count+=1
        while x >= 5:
            x-=5
            count+=1
        print(count)


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
