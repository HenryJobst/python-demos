class Auto:

    def __init__(self, farbe='Rot'):
        self.__farbe = farbe

    def get_farbe(self):
        return self.__farbe

    def __eq__(self, other):
        return self.__farbe == other.__farbe

auto1 = Auto('Grün')
auto2 = Auto('Blau')

print(f'{auto1 == auto2}')
print(id(auto1) == id(auto2))

print(f'Die Farbe von Auto 1 ist {auto1.get_farbe()}.')

print(f'Die Farbe von Auto 2 ist {auto2.get_farbe()}.')