class Girl:
    #class variable
    gender = 'f'

    #name: instance variable
    def __init__(self, name):
        self.name = name

rachel = Girl('rachel')
stanky = Girl('Stanky')

print(rachel.gender)
print(rachel.name)
print(stanky.gender)
print(stanky.name)
