"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def get_fib(position):
    aux = 1
    value = 1
    if aux >= position:
        return position
    else:
        print(f"aux: {aux}, value: {value}")
        aux += 1
        value += get_fib(aux)
        return value


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
