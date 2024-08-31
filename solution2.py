# takes a string text as input and returns the count of vowels (a, e, i, o, u) in the string. Ignore case sensitivity.
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    total_vowels = sum(text.count(vowel) for vowel in vowels)
    return total_vowels

print(count_vowels('python is a cool language'))       


#  takes a non-negative integer n as input and returns the factorial of that number
def calculate_factorial(n):
    if n < 0:
         return "Factorial not applicable to negative numbers"
    elif n == 0:
         return 1
    
    factorial = 1
  # iterates thru numbers from 1 to n and multiplies each i with the current value of factorial
    for i in range (1, n+1):
        factorial = factorial * i
    return factorial  
   
print(calculate_factorial(5))     


# takes a function func as input and applies a decorator named decorator_func.
def apply_decorator(func):
    
    def decorator_func():
        print("Decorator Applied")
        func()
    return decorator_func  
print(apply_decorator)