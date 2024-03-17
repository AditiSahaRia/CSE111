#Example 1:
my_family = {
    'child_01' : {
        'name' : 'Emil',
        'year' : 2004
    },
    'child_02' : {
        'name' : 'Tobi',
        'year' : 2007
    },
    'child_03' : {
        'name' : 'Luna',
        'year' : 2011
    }

}

print(my_family)

#Example 2

child_01 = {
        'name' : 'Luna',
        'year' : 2011
    }
child_02 = {
        'name' : 'Emil',
        'year' : 2004
    }
my_family = {
    'child_01' : child_01,
    'child_02' : child_02
}

print(my_family)