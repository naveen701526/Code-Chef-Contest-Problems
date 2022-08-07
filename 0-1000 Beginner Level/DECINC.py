import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    print( n + 1 if not n % 4 else n - 1 )


answer_finder()