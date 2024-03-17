#get vs [] for retrieving elements

my_dict = {'name': 'Jack', 'age': 26}

print(my_dict['name'])

print(my_dict.get('age')) #another way


# Trying to access keys which doesn't exist throws error

#Output None

print(my_dict.get('address'))


#keyError
#print(my_dict['address'])