import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    arr = [int(x) for x in input().split()]
    new = set(arr)
    arr = len(arr)
    new = len(new)
    if new <= 2:
        print('YES')
    else:
        print('NO')
    


answer_finder()