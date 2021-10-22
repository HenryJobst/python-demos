# Variante 1 - Deklaration
def function1(param1):
    print(param1)


# Variante 2 - Deklaration
def function2(param1, param2=20):
    print(param1, param2)


def function2b(param1=10, param2=20):
    print(param1, param2)


# Variante 3 - Deklaration
def function3(*args):
    print("---")
    for arg in args:
        print(arg)


# Variante 4 - Deklaration
def function4(**param):
    print("---")
    for item in param.items():
        print(item)


# Kombination der Varianten 1-4 - Deklaration
def function5(param1, param2=20, *param3, **param4):
    print(param1, param2, param3, param4)


# Variante 1 - Aufruf
function1(10)

# Variante 2 - Aufruf
function2(10, 30)
function2(10)
function2(param2=10, param1=20)

# Variante 3 - Aufruf
function3()
function3(10)
function3(10, 20)
function3(10, 10, 30, 46, 36, 90)

# Variante 4 - Aufruf
tupleParam = (1, 2)
function4()
function4(key1='value1')
function4(key1='value1', key2='value2')

# Kombination der Varianten 1-4 - Aufruf
function5(10)
function5(11, 21)
function5(12, 22, 23, 24, key1=12)
