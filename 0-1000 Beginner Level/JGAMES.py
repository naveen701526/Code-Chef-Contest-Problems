import sys
from tkinter import Y
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y = [int(x) for x in input().split()]
    val = x + y
    if val%2:
        print('Jay')
    else:
        print('Janmansh')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
