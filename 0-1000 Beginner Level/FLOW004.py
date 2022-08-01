def answer_finder():
    n = input()
    print(int(n[0])+int(n[-1]))



test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()