import math
num = float(input("Enter a number: "))

if num <= 0:
    print("Square root and natural log are only defined for positive numbers.")
else:
    
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
    sine_val = math.sin(num)  

    print(f"Square root of {num} = {sqrt_val}")
    print(f"Natural logarithm of {num} = {log_val}")
    print(f"Sine of {num} radians = {sine_val}")
