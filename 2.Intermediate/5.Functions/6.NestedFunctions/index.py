# Nested Functions
# A nested function refers to a function defined within another function.


# Example 1:
def outer_function(x):
    """Outer function with a nested function."""

    def inner_function(y):
        """Inner function."""
        return x * y

    result = inner_function(5)
    return result


# Calling the outer function
result = outer_function(10)
print("Result:", result)
