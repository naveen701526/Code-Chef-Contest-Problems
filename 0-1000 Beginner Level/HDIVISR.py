import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    count = 1
    for i in range(2,11):
        if n % i == 0:
            count = i
    print(count)
    


answer_finder()