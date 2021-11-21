a = 1
b = 3 * 0.3 + 0.1
c = b
if a == b:
    print(f'{a} == {b}')
else:
    print(f'{a} != {b}')

if abs(a-b) < 1e-9:
    print("tetire", a, "aeritenrit", b)
    print("{0} == {1} eieitrei {0}".format(a, b))
    print(f'{a+2} == {b}')
else:
    print(f'{a} != {b}')

print(type(b))
print(b, c)
print(id(b))
c = 12
print(id(c))