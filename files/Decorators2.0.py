def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function ran!")

# display()

# but if the display function takes in arguments this won't work unless we add *args and **kwargs
@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments {name},{age}")

display_info("David", 19)