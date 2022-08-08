import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    
    n,k,x,y = [int(x) for x in input().split()]
    val = x*k
    val1 = min(x,y)
    val2 = (n-k)*val1
    print(val+val2)

    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
