squares = {1: 1, 3: 9, 4: 16, 5: 25}

print(1 in squares)
print(49 in squares)
print(25 in squares)   #Though 25 is present in the dictionary but it's not a key value.
print(2 not in squares)

#Membership test only returns BOOLEAN values