import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y = [int(x) for x in input().split()]
    val1 = 500 - x*2
    val2 = 1000 - (x+y)*4
    temp1 = val1 + val2
    val1 = 500 - (x+y)*2
    val2 = 1000 - (y)*4
    temp2 = val1 + val2
    print(max(temp1, temp2))
    
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
