

def solve():
    number_arr = [int(x) for x in input().split()]
    print(max(number_arr[0], number_arr[1])+max(number_arr[2], number_arr[3]))


test_cases = int(input())

while(test_cases):
    test_cases -= 1
    solve()
