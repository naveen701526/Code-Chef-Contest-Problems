

def solve():
    temperature = int(input())
    if temperature > 20:
        print('HOT')
    else:
        print('COLD')


test_cases = int(input())

while(test_cases):
    test_cases -= 1
    solve()
