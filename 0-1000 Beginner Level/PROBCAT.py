import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x = int(input())
    if x in range(1, 100):
        print('Easy')
    elif x in range(100,200):
        print('Medium')
    elif x in range(200, 301):
        print('Hard')
        
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
