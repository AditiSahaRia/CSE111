def fibonacci(num):
    f=0
    s=1
    print(f,end=" ")
    print(s,end=" ")
    for num in range(1,10):
        if f+s>10:return
        t=f+s
        f=s
        s=t
        print(t,end=" ")
fibonacci(10)

print()
print('2nd try : ')

def fibonacci(num):
    f = 0
    s = 1
    print(f, end=" ")
    print(s, end=" ")
    for num in range(1, num):
        if f + s < num:
            t = f + s
            f = s
            s = t
            print(t, end=" ")


fibonacci(5)