def answer_finder():
    arr = [int(x) for x in input().split()]
    arr.sort(reverse=True)
    print(arr[1])
    

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()