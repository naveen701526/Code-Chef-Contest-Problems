def answer_finder():
    n = int(input())
    arr = [int(x) for x in input().split()]
    count = 0
    val = [2,3,9]
    for i in range(arr[0], arr[-1]+1):
        if i%10 in val:
            count+=1
    print(count)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()