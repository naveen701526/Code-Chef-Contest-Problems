import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    values = input().split()
    dis = {
        'R': 1,
        'B': 2,
        'G': 3
    }
    if dis[values[0]] < dis[values[1]]:
        print(values[0])
    else:
        print(values[1])
    


answer_finder()
