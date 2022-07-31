def answer_finder():
    arr = [int(x) for x in input().split()]
    print(min(arr[0]+arr[1], arr[2]+arr[3]))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()