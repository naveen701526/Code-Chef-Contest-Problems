def answer_finder():
    s = input()
    t = input()
    m = ''
    for i in range(len(s)):
        if s[i] == t[i]:
            m+='G'
        else:
            m+='B'
    print(m)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()