import math

# Given
def is_number(n):
    try:
        float(n)    # Type-casting the string to ‘float‘.
                    # If string is not a valid ‘float‘,
                    # it’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


# Activation Functions
def sigmoid(x):
    return f"sigmoid: f({x})= {1 / (1 + math.exp(-x))}"


def relu(x):
    return f"relu: f({x})= {max(0, x)}"


def elu(x, alpha = 0.01):
    if x > 0:
        return f"elu: f({x})= {x}"
    else:
        return f"elu: f({x})= {alpha * (math.exp(x) - 1)}"

 
def activation_function(x, func):    
    x = float(x)

    if func == "sigmoid":
        return sigmoid(x)
    elif func == "elu":
        return elu(x)
    elif func == "relu":
        return relu(x)
    else:
        return f"{func} is not support"
    
def exercise2():
    x = input('Input x: ')

    if not is_number(x):
        return "x must be a number"

    func = input('Input activation Function (sigmoid|relu|elu): ') 

    return activation_function(x, func)

print(exercise2())