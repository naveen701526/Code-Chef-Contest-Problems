import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder(n):
    arr = [0]
    arr1 = [int(x) for x in input().split()]
    arr = arr + arr1

    for i in range(1, n+1):
        if i != arr[arr[i]]:
            print('not ambiguous')
            return
    print('ambiguous')


while True:
    n = int(input())
    if n == 0:
        break
    else:
        answer_finder(n)
