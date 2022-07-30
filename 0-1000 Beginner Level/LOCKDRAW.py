def answer_finder():
    arr = [int(x) for x in input().split()]
    arr.sort(reverse=True)
    alice = arr[0]
    for i in range(1, len(arr)):
        if alice != 0:
            alice-=arr[i]
        else:
            alice+=arr[i]
    print('YES' if alice == 0 else 'NO')


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()