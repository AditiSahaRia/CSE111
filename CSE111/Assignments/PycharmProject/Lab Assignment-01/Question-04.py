class Joker:
    def __init__(self, x, y, z):
        self.name = x
        self.power = y
        self.is_he_psycho = z

j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print(' == == == == == == == == == == =')
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print(' == == == == == == == == == == =')
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')

print('''The first if else block checks weather j1 and j2 both objects refers to the same memory location or not. We know that different objects reserves different memory location. That's why the first if else block prints "different"''')
print('''The second if else block checks weather the name of both j1 and j2 object is same or not. AS the names are same that's why the output shows "same"''')