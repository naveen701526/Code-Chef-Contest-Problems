def answer_finder():
    n = int(input())
    
    print('Good' if not n%4 else 'NOT GOOD')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()