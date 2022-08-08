import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')





c = input()
c = c.lower()
if c in ['a','e','i','o','u']:
    print('Vowel')
else:
    print('Consonant')
