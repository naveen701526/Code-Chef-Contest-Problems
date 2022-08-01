def answer_finder():
    exp = input()
    operator = []
    ans = ''
    for i in exp:
        if i == '(':
            continue
        elif i == ')':
            temp = operator.pop()
            ans+=temp
            continue
        elif i in ['*','+','-','^','/']:
            operator.append(i)
            continue
        ans+=i
    print(ans)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()