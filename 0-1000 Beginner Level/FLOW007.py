def answer_finder():
    n = int(input())
    ans = 0
    while n>0:
        ans = ans*10 + n%10
        n//=10
    print(ans)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()