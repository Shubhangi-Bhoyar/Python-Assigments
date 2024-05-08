a = int(input("a:",))
b = int(input("b:",))
def calculation(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    return add , sub , mul
res = calculation(a,b)
print(res)
