# takes two parameters (num1 and num2), and returns the sum of the two numbers.
def add_numbers(num1, num2):
     return num1 + num2

print(add_numbers(2,4) ) 


# takes a single parameter (number) and returns True if the number is even, and False if otherwise.
def is_even(number):
    if number % 2 ==0:
         return True
    else:
         return False
    
print(is_even(30))    
print(is_even(33))    


# takes a string (text) as input and returns the reversed version of that string.
def reverse_string(text):
    #  reverse the input (text)
     reversed_text = "".join(reversed(text))
     return reversed_text
    
print(reverse_string("word"))     
print(reverse_string("race car here"))     
