import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


a,b = [int(x) for x in input().split()]

if a > b:
    print(a-b)

else:
    print(a+b)

    