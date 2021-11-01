# leere Liste
liste1 = []
print(liste1)

# Liste mit 3 statischen Strings
liste2 = ['A', 'B', 'C']
print(liste2)


# (Prädikats-)Funktion mit Typannotationen
def is_valid(i: int) -> bool:
    return i % 2 == 0


# list comprehension
liste3 = [pow(i, 2) for i in range(10) if is_valid(i)]
print(liste3)
# Equivalenter Code zur vorhergehenden list comprehension
liste3 = []
for i in range(10):
    if is_valid(i):
        liste3.append(pow(i, 2))

list4 = [pow(i, 3) for i in range(20) if is_valid(i)]
print(list4)

# set comprehension
set1 = {0 for _ in range(10)}
print(set1)

# dict comprehension
dict1 = {i: pow(i, 2) for i in range(10)}
print(dict1)

# verschachtelte dict comprehension
liste5 = [a + b for a in range(10) for b in range(5)]
print(liste5)
# das Equivalent
liste5 = []
for a in range(10):
    for b in range(5):
        liste5.append(a+b)
