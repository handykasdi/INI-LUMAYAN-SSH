ListofAlphabet = ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def short():
    for i in separate:
        if i in ListofAlphabet:
            print(i, end="")
    return

while True:
    please = input("\nplease input firstname & lastname: ")
    last_names = please.title()
    separate = list(last_names)
    print("Result: ",end=" ")
    short()
