def answer_finder():
    n = int(input())
    if n == 0 or n == 1:
        print(1)
    elif n < 0:
        print(-1)
    else:
        val = 1
        for i in range(1,n+1):
            val*=i
        print(val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()