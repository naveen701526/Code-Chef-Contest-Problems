import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


while True:
    val = int(input())
    if val == 42:
        break
    else:
        print(val)