#key restrictions
MLB_team = {'k': 'Twins'}
MLB_team['k'] = 'Hi' #It will replace existing value
print(MLB_team)

MLB_team = {'key': 'Hi', 'key': 'hello'} #It will not add two key of same name. It will replace existing value

print(MLB_team)

#d = {[1,1]: 'a', [1,2]: 'b'[2,1]: 'c', [2,2]: 'd'} #TypeError