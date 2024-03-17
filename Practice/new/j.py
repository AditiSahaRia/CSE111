#n = int(input())
#for i in range(2,n):
 #   if n%i==0:
  #      print(f'{i}{n//i}')
   #     break
#else:
  #  print(-1)
count1 = 0
count2 = 0
count3 = 0
for i in range(100,1000):
    if (i%6==2):
        count1 += 1
    if (i%9==5):
        count2 += 1
    if (i%11==7):
        count3 += 1

print(count1)
print(count2)
print(count3)