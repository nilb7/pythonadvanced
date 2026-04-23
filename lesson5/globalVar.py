def test():
    name = "Lisa"
    print(name)

test()

shkolla = "Digitalschool"

def test2():
    global shkolla
    shkolla = "Harvard"

test2()
print(shkolla)