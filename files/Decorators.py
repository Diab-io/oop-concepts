def decorator_function(original_function):
    def wrapper_function():
        print(f"This function ran before {original_function.__name__}")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("display function ran!")

display()


# The above is the same as the below

# def display():
#     print("display function ran!")

# decorated_display = decorator_function(display)
# decorated_display()