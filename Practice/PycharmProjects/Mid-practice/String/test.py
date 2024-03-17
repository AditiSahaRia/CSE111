st=input("=>")
st = st.lower()
fi=[]
for i in st :
    count = 0
    if i in fi :
        pass
    else :
        for j in st :
            if i == j :
                count += 1
        fi.append(i)
        for k in range(count):
            print(i,"=",count,end=' ')
