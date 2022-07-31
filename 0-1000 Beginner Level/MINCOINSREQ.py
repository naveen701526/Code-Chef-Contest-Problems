def answer_finder():
    x = int(input())
    count = 0
    while 10 <= x:
        count+=1
        x-=10
    print(x)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()