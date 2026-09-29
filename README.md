# Number Toolkit

Number Toolkit is a small Python program made for practicing basic number algorithms.

It runs in the terminal and gives the user a menu from which different operations can be selected. The project includes factorial, Fibonacci numbers, GCD, prime checking, prime factors, and reversing the digits of a number.

## What can it do?

The program has these options:

* Find the factorial of a number
* Find the Fibonacci number at a particular position
* Find the GCD of two numbers
* Check whether a number is prime
* Find the prime factors of a number
* Reverse the digits of a number
* Exit the program

## Requirements

You only need **Python 3** to run this project.

There are no third-party packages or extra libraries to install.

To check your Python version, open a terminal and run:

```bash
python --version
```

On some systems, you may need to use:

```bash
python3 --version
```

## Getting the Project

Clone the repository using:

```bash
git clone https://github.com/{github-username}/{repo-name}.git
```

Then move into the project folder:

```bash
cd {repo-name}
```

Replace the username and repository name with the actual details of the GitHub repository.

## Running the Program

Once you are inside the project folder, run:

```bash
python number_toolkit.py
```

If `python` is not the command used on your computer, try:

```bash
python3 number_toolkit.py
```

After starting, you will see a menu like this:

```text
===== Number Toolkit =====
1. Factorial
2. Nth Fibonacci number
3. GCD of two numbers
4. Prime check
5. Prime factors
6. Reverse a number
7. Exit
```

Enter the option number and then provide the required input.

## Some Examples

### 1. Factorial

```text
Pick an option (1-7): 1
Enter a number (0 or more): 5
5! = 120
```

### 2. Fibonacci

```text
Pick an option (1-7): 2
Which position? 7
Fibonacci number at position 7 is 13
```

### 3. GCD

```text
Pick an option (1-7): 3
First number: 24
Second number: 36
GCD(24, 36) = 12
```

### 4. Prime Check

```text
Pick an option (1-7): 4
Enter a number: 17
17 is prime.
```

### 5. Prime Factors

```text
Pick an option (1-7): 5
Enter a number (2 or more): 60
Prime factors of 60: [2, 2, 3, 5]
```

### 6. Reverse a Number

```text
Pick an option (1-7): 6
Enter a number (0 or more): 12345
Reversed: 54321
```

To close the program, choose option `7`.

## Input Handling

The program checks the input before using it. If something other than an integer is entered, it asks the user to enter the value again.

There are also some restrictions depending on the operation. For example, factorial accepts `0` and positive numbers, while the prime-factor option requires a number of at least `2`.

This is handled by the `get_int()` function in the program.

## Main Functions

The Python file contains separate functions for the different operations:

* `get_int()` — takes integer input and checks it
* `find_factorial()` — calculates factorial
* `find_fibonacci()` — finds a Fibonacci number
* `find_gcd()` — finds the GCD using Euclid's method
* `check_prime()` — checks if a number is prime
* `get_prime_factors()` — finds the prime factors
* `reverse_digits()` — reverses a number
* `show_menu()` — prints the menu
* `main()` — runs the program and handles the user's choices

Keeping the operations in separate functions makes the program easier to follow and modify.

## Concepts Used

This project uses basic Python concepts such as:

* Functions
* `if` / `else` statements
* `for` and `while` loops
* User input
* Integer arithmetic
* Modulo (`%`)
* Lists
* Basic number algorithms
* Input validation

## Project Files

The repository contains:

```text
Number-Toolkit/
│
├── number_toolkit.py
└── README.md
```

`number_toolkit.py` contains the actual program, while this `README.md` explains how to set it up and use it.

## Final Note

This is a simple command-line project made to put several basic number algorithms together in one program. It does not need any special setup apart from having Python 3 installed.

## Author

**SHASHWAT CHOUHAN**

Python Essentials Course
