def answer_finder():
    res = [
        6,
        2,
        5,
        5,
        4,
        5,
        6,
        3,
        7,
        6

    ]
    arr = [int(x) for x in input().split()]
    ans = sum(arr)
    ans = str(ans)
    val = 0
    for i in ans:
        val += res[int(i)]
    print(val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()