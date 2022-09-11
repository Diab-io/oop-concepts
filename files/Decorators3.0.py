#using classes as decorators

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args,**kwargs):
        print(f"call method executed before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print("display function ran!")

# display()

# but if the display function takes in arguments this won't work unless we add *args and **kwargs
@decorator_class
def display_info(name, age):
    print(f"display_info ran with arguments ({name},{age})")

display_info("David", 19)