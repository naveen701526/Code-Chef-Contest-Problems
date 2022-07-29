

def solve():
    n = int(input())
    string1 = input()
    string2 = input()
    count = 0
    for i in range(n):
        if string1[i] != string2[i]:
            count += 1
    if count % 2 == 0:
        print('1')
    else:
        print('0')


test_cases = int(input())

while test_cases:
    test_cases -= 1
    solve()
