test_case = int(input())
for j in range(test_case):
    number = int(input())
    count = 0
    for i in range(2,10,1):
        if number/i<=10:
            count += 1
            break
    if count>=1:
        print('Yes')
    else:
        print('No')