import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')

l = int(input())
b = int(input())
peri = 2*(l+b)
area = l*b
if area > peri:
    print('Area')
    print(area)
elif peri > area:
    print('Peri')
    print(peri)
elif peri == area:
    print('Eq')
    print(area)

    

    
    
   