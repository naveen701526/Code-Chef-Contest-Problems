def answer_finder():
    n, x = [int(x) for x in input().split()]
    if n <=6:
        print(x)

    else:
        val = 0
        while n > 0:
            n-=6
            val+=x
        print(val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()