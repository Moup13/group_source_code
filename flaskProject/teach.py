def button(func):
    def wrapper():
        prunt()
        func()
        print("\__________/")
    return wrapper