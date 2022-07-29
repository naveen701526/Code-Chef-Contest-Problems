def answer_finder():
    n = int(input())
    if n < 0 or (n % 10 == 0 and n != 0):
        print('loses')

    else:
        reversed_num = 0
        while n > reversed_num:
            reversed_num = reversed_num*10 + n % 10
            n //= 10
        print('wins' if n == reversed_num or n ==
              reversed_num//10 else 'loses')


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()
