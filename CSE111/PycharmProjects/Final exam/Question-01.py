#Question-01

#Name : Aditi Saha Ria
#ID : 20101238
#Section : 07
#Course Code : CSE111


series_dictionary = {}

value_of_k = int(input())

checking_value = int(input())

series_value = 0
value_index = 0
i = 1

while series_value <= value_of_k:
    series_value = int((2*i*((2*i)-1))/2)
    if series_value>value_of_k:
        break
    else:
        series_dictionary[i] = series_value


    i += 1

print(series_dictionary)

for k in range(1, len(series_dictionary)):
    if series_dictionary[k] == checking_value:
        print(f'Key: {k}, Value: {series_dictionary[k]}')
        break

else:
    print('no such value exists')

