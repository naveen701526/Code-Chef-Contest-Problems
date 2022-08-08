import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n, x = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    sums = sum(arr)
    count = 0
    while True:
        val = sums + count
        val = val/n
        if val >= x:
            break
        count+=1
    print(count)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
