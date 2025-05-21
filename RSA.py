import random

# ANSI color codes for a new color scheme
CYAN = '\033[36m'
MAGENTA = '\033[35m'
WHITE = '\033[97m'
RED = '\033[91m'
RESET = '\033[0m'

# Function to compute GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        raise Exception("Modular inverse does not exist.")
    else:
        return x % phi

# Prime check
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Key generation with detailed output
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError(f'{RED}Error: Both numbers must be prime.{RESET}')
    elif p == q:
        raise ValueError(f'{RED}Error: p and q cannot be equal.{RESET}')
    elif p < 10 or q < 10:
        raise ValueError(f'{RED}Error: Choose larger primes (>= 10) for proper functionality.{RESET}')

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    # Print detailed calculations with new colors
    print(f"\n{CYAN}Calculated Values:{RESET}")
    print(f"{MAGENTA}n  = p * q = {p} * {q} = {n}{RESET}")
    print(f"{MAGENTA}φ(n) = (p - 1) * (q - 1) = {p - 1} * {q - 1} = {phi}{RESET}")
    print(f"{WHITE}e  (encryption exponent) = {e}{RESET}")
    print(f"{WHITE}d  (decryption exponent) = {d}{RESET}")
    print(f"\n{CYAN}Public Key (e, n): ({e}, {n}){RESET}")
    print(f"{CYAN}Private Key (d, n): ({d}, {n}){RESET}\n")

    return ((e, n), (d, n))

# Encryption
def encrypt(pk, plaintext):
    key, n = pk
    return [(ord(char) ** key) % n for char in plaintext]

# Decryption
def decrypt(pk, ciphertext):
    key, n = pk
    decrypted_values = [(char ** key) % n for char in ciphertext]
    print(f"\n{WHITE}Decrypted numeric values:{RESET}", decrypted_values)
    decrypted_chars = []
    for val in decrypted_values:
        if 32 <= val <= 126:
            decrypted_chars.append(chr(val))
        else:
            decrypted_chars.append('?')  # Fallback for non-printable chars
    return ''.join(decrypted_chars)

# Main program
def main():
    print(f"\n{CYAN}RSA Algorithm Implementation{RESET}\n")

    try:
        p = int(input(f"{MAGENTA}Enter a prime number p: {RESET}"))
        q = int(input(f"{MAGENTA}Enter a prime number q: {RESET}"))

        public_key, private_key = generate_keypair(p, q)

        message = input(f"{MAGENTA}Enter a message to encrypt: {RESET}")
        encrypted_msg = encrypt(public_key, message)
        print(f"\n{WHITE}Encrypted message:{RESET}", encrypted_msg)

        decrypted_msg = decrypt(private_key, encrypted_msg)
        print(f"{WHITE}Decrypted message:{RESET}", decrypted_msg)

    except ValueError as ve:
        print(f"{RED}Error:{RESET} {ve}")
    except Exception as e:
        print(f"{RED}Exception:{RESET} {e}")

# Corrected entry point
if __name__ == "__main__":
    main()
