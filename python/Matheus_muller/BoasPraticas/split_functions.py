def is_prime_number(a: int) -> bool:
    return a % 2

def main():
    print(is_prime_number(10))
    print(is_prime_number(100))
    print(is_prime_number(1000))
    print(is_prime_number(100000))
    print(is_prime_number(10000))
    print(is_prime_number(10000000))
    print(is_prime_number(100000001))

if __name__ == "__main__":
    main()