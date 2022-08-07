import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    p,q = [int(x) for x in input().split()]
    toggle = 'Bob'
    
    
    i = 0
    while i <= p+q:
        toggle = 'Bob' if toggle=='Alice' else 'Alice'
        i+=2
    print(toggle)


        
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
