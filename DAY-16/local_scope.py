def Outer():
    print("Enclosing Scope")

    def Inner():
        print("Local Scope")

    Inner()
    print("Outer Function")

print("Start")

Outer()

print("End")