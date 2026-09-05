a = 10
def Outer():
    a = 50

    def Inner():
        nonlocal a
        a = 100
        print("Inside Inner():", a)

    Inner()
    print("Inside Outer():", a)

print("Start")

Outer()

print("End")