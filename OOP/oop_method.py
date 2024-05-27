def my_function(x):
    my_function.call_count = getattr(my_function, "call_count", 0) + 1
    return x * x
print(my_function.call_count)
print(my_function(5))  # Output: 25
print(my_function(10)) # Output: 100
print(my_function.call_count)  # Output: 3