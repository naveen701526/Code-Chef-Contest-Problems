import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    r,o,c = [int(x) for x in input().split()]
    rem = 20 - o
    max_runs = rem*36
    val = r -c
    if max_runs > val:
        print('YES')
    else:
        print('NO')
    


answer_finder()