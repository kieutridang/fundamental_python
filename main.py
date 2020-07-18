a = 20
b = 20

if (id(a) == id(b)):
    print("same id")
else:
    print("not same id")
    print("a id: %s, b id: %s" % (id(a), id(b)))
