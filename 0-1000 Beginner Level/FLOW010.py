import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    c = input().lower()
    if c == 'b':
        print('BattleShip')
    elif c == 'c':
        print('Cruiser')
    elif c == 'd':
        print('Destroyer')
    else:
        print('Frigate')
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
