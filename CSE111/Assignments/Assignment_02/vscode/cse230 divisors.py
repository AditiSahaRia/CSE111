count = 0
for i in range(6,501,1):
    if i%6==0 or i%9==0:
        count += 1
print(count)