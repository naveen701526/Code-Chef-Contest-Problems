import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    ans = 0
    d = [100,50,10,5,2,1]
    for i in d:
        while n >= i:
            ans+=1
            n-=i
    print(ans)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
