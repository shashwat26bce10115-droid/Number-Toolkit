# Number Toolkit
# Small menu program for the basic number algorithms we covered in class.


def get_int(prompt, min_value=None):
    # keeps asking until the user types a proper integer
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("That's not a valid integer, try again.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number that is at least {min_value}.")
            continue
        return value


def find_factorial(num):
    answer = 1
    for i in range(2, num + 1):
        answer = answer * i
    return answer


def find_fibonacci(pos):
    # fib(0) = 0, fib(1) = 1, fib(2) = 1, ...
    prev, curr = 0, 1
    for _ in range(pos):
        prev, curr = curr, prev + curr
    return prev


def find_gcd(x, y):
    # Euclid's method: keep replacing (x, y) with (y, x % y)
    x, y = abs(x), abs(y)
    while y:
        x, y = y, x % y
    return x


def check_prime(num):
    if num < 2:
        return False
    # only need to test divisors up to sqrt(num)
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True


def get_prime_factors(num):
    result = []
    d = 2
    while d * d <= num:
        while num % d == 0:
            result.append(d)
            num //= d
        d += 1
    if num > 1:  # whatever is left over is itself a prime
        result.append(num)
    return result


def reverse_digits(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev


def show_menu():
    print("\n===== Number Toolkit =====")
    print("1. Factorial")
    print("2. Nth Fibonacci number")
    print("3. GCD of two numbers")
    print("4. Prime check")
    print("5. Prime factors")
    print("6. Reverse a number")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Pick an option (1-7): ").strip()

        if choice == "1":
            n = get_int("Enter a number (0 or more): ", 0)
            print(f"{n}! = {find_factorial(n)}")

        elif choice == "2":
            n = get_int("Which position? ", 0)
            print(f"Fibonacci number at position {n} is {find_fibonacci(n)}")

        elif choice == "3":
            a = get_int("First number: ")
            b = get_int("Second number: ")
            print(f"GCD({a}, {b}) = {find_gcd(a, b)}")

        elif choice == "4":
            n = get_int("Enter a number: ")
            if check_prime(n):
                print(f"{n} is prime.")
            else:
                print(f"{n} is not prime.")

        elif choice == "5":
            n = get_int("Enter a number (2 or more): ", 2)
            print(f"Prime factors of {n}: {get_prime_factors(n)}")

        elif choice == "6":
            n = get_int("Enter a number (0 or more): ", 0)
            print(f"Reversed: {reverse_digits(n)}")

        elif choice == "7":
            print("Bye!")
            break

        else:
            print("Invalid option, choose between 1 and 7.")


if __name__ == "__main__":
    main()
