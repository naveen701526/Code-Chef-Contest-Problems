import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    arr = [int(x) for x in input().split()]
    val = min(arr)
    idx = arr.index(val)
    arr.pop(idx)
    print(sum(arr))
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
