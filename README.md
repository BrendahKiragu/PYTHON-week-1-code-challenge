# PYTHON WEEK 1 CODE CHALLENGE

## Overview

This repository contains solutions to a series of Python programming challenges covering basic data structures, functions, decorators, sequences, sets, dictionaries, and object-oriented programming.

---

## Table of Contents

- [Topics Covered](#topics-covered)
- [File Structure](#file-structure)
- [Solutions](#solutions)
  - [solution1.py](#solution1py)
  - [solution2.py](#solution2py)
  - [solution3.py](#solution3py)
- [Setup and Running Instructions](#setup-and-running-instructions)
- [Submission Guidelines](#submission-guidelines)

---

## Topics Covered

- Basic Data Structures
- Functions
- Decorators
- Sequences
- Sets and Dictionaries
- Object-Oriented Programming

---

## File Structure

The repository is organized as follows:

├── solution1.py ├── solution2.py ├── solution3.py └── README.md


- _solution1.py:_ Contains basic functions for arithmetic, string manipulation, and condition checking.
- _solution2.py:_ Includes functions for working with lists, counting elements, and applying decorators.
- _solution3.py:_ Focuses on sorting, dictionary operations, and object-oriented programming.

---

## Solutions

### solution1.py

1. **`add_numbers(num1, num2)`**
   - Adds two numbers and returns the result.
   - **Returns:** `int` or `float` - The sum of `num1` and `num2`.

2. **`is_even(number)`**
   - Checks if a number is even and returns `True` if even, `False` if odd.
   - **Returns:** `bool`.

3. **`reverse_string(text)`**
   - Reverses a given string and returns the reversed version.
   - **Returns:** `str`.

---

### solution2.py

4. **`count_vowels(text)`**
   - Counts the number of vowels in a given string.
   - **Returns:** `int` - The number of vowels found.

5. **`calculate_factorial(n)`**
   - Calculates the factorial of a non-negative integer `n` and returns the factorial value. Returns a message if `n` is negative.
   - **Returns:** `int` for non-negative numbers, or a string message for invalid input.

6. **`apply_decorator(func)`**
   - Applies a decorator that prints "Decorator Applied" before calling the original function `func`.
   - **Returns:** Wrapped function with the applied decorator.

---

### solution3.py

7. **`sort_by_age(sample_tuple)`**
   - Sorts a list of tuples based on the second element (age) in ascending order.
   - **Returns:** `list` - Sorted list of tuples.

8. **`merge_dicts(dict1, dict2)`**
   - Merges two dictionaries into a single dictionary.
   - **Returns:** `dict` - The merged dictionary.

9. **`Car` class**
   - Defines a `Car` class with attributes `make`, `model`, and `year`.
   - Includes a method `display_info()` to print the car's information.

---

## Setup and Running Instructions

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/python-week1-challenge.git

2.  Navigate to the project directory:
     cd python-week1-challenge

3. Run any solution script on the terminal as follows:
     python3 solution1.py 
     python3 solution2.py 
     python3 solution3.py 
