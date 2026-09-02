'''
x=100
def name():
    global x
    x=5
    print(x)
name()
print(x)
'''
def outer():
    x=100
    def inner():
        nonlocal x
        x=49

    inner()
    print(x)

outer()