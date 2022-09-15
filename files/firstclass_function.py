# A programming language is said to have first class functions if it treats functions
# as first class citizens

# First-class citizen(programming)
# A first-class citizen is an entity which supports all the operations generally
# available to other entities
# These operations typically include being passed as an argument, returned from a function
# assigned to a variable

#!/usr/bin/python3
def square(x):
    return x * x

f = square #Assigned a function to a variable
print(square)
print(f(5))

# Higher order function: A function that accepts annother function as argument
# or a function that returns another function

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

# passing a function as an argument
squares = my_map(square, [1,2,3,4,5])
cubes = my_map(cube, [1,2,3,4,5])

print(squares)
print(cubes)




# returning a function from a function
def logger(msg):
    
    def log_message():
        print('log:',msg)
    
    return log_message

log_hi = logger("Hi!")
log_hi()


def html_tag(tag):
    
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>\n")
    
    return wrap_text

print_h1 = html_tag('h1')
print_h1("Testing Headline!")
print_h1("Another Headline")

print_p = html_tag('p')
print_p("This is a paragraph")
print_p("This is another paragraph")