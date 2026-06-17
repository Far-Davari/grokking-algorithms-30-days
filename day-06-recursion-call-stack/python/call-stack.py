def greet(name):
    print("hello " + name + "!")
    greet2(name)
    print("greeting ready to say bye...")
    bye()

def greet2(name):
    print("how are you " + name + "?")

def bye():
    print("OK bye!")

greet("farshad")

