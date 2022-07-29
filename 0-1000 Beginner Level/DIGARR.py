def answer_finder():
    n = int(input())
    s = input()
    ans = ''
    
    for c in s:
        if c=='5' or c == '0':
            ans+=c
            
            break
    if ans == '':
        print('No')
    else:
        print('Yes')


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()