n = int(input())

if n%2==1:
    print('Weird')
elif n==2 or n==4:
    print('Not Weird')
elif n%2==0 and (n!=2 or n!=4) and n<=20:
    print('Weird')
elif n%2==0 and n>20 :
    print('Not Weird')