def answer_finder():
    n = input()
    count = 0
    for i in n:
        if i == '4':
            count+=1
    print(count)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()