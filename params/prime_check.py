# Write your code below this line 👇


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            # Not a prime
            is_prime = False
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
