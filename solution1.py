def add_numbers(num1, num2):
     return num1 + num2
print(add_numbers(2,4) ) 


def is_even(number):
    if number % 2 ==0:
         return True
    else:
         return False
print(is_even(30))    
print(is_even(33))    


def reverse_string(text):
    #  reverse the input (text)
     reversed_text = "".join(reversed(text))
     return reversed_text
    
print(reverse_string("word"))     
print(reverse_string("race car here"))     


def count_vowels(text):
    vowels = 'aeiouAEIOU'
    total_vowels = sum(text.count(vowel) for vowel in vowels)
    return total_vowels

print(count_vowels('python is a cool language'))       


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
