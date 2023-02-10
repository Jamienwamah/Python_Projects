def d():
    animal = "dog"
    def e():
        nonlocal animal
        animal = "cat"
        print("Inside nested function: " + animal)
    print("Before calling function: " + animal)
    e()
    print("After nested function: " + animal)
    
animal = "horse"
d()
print("Global animal: " + animal)
    