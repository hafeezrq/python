x = "awesome variable!"

def myfunc():
    print(x)
    print(id(x))

def anotherfunc():
    y = 5
    while y >= 1:
        print(id(y))
        y -= 1

myfunc()
anotherfunc()