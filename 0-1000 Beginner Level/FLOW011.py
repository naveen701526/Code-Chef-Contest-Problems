import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    salary = int(input())
    if salary < 1500:
        hra = 0.1*salary
        da = 0.9*salary
        ans = salary + hra + da
        print(ans)
    else:
        hra = 500
        da = 0.98*salary
        ans = salary + hra + da
        print(ans)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
