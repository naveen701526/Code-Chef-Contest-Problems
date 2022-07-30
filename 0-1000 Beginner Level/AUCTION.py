def answer_finder():
    a,b,c = [int(x) for x in input().split()]
    if a > max(b,c):
        print('Alice')
    elif b > max(a,c):
        print('Bob')
    else:
        print('Charlie')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()