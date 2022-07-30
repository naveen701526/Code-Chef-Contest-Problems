def answer_finder():
    n = int(input())
    a = [int(x) for x in input().split()]
    val = 0
    for i in a:
        if i < 1000:
            val+=1
    print(n - val)


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()