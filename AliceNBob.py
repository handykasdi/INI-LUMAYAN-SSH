contoh = {"Odd": "Alice", "Even": "Bob"}

#function to print winner
def siapamenang():
    if sample in even:
        print("The Winner is", contoh["Even"])
    elif sample == 0:
        print("SORRY ERROR BRO")
        #Basically do nothing
    else :
        print("The Winner is", contoh["Odd"])

sample = int(input("Any Number to Decide Who Win : "))
even =  [value*2 for value in range(1,sample+1)]
siapamenang()
