def answer_finder():
    x,y,z = [int(x) for x in input().split()]
    count = 0
    while x > 0:
        count+=z
        x-=y
    print(count)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()

