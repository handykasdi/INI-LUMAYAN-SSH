#Number 4:
asd = "a"
posisi =1

def x():
    global asd
    v= input("Either a, b, c only ")
    k= v.lower()
    asd = k
    formulae()
    return v, k, asd
#fucked up
x()
