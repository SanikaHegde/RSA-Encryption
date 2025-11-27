
# RSA Encryption in Python

This project is a simple implementation of the RSA cryptographic algorithm in Python.  
It allows you to:

- Generate public and private keys from two prime numbers.
- Encrypt messages using the public key.
- Decrypt messages using the private key.

## Features

- Uses the Extended Euclidean Algorithm to find the modular inverse.
- Validates prime numbers for key generation.
- Provides detailed console output with colored text for better readability.
- Handles encryption and decryption of text messages.

## How to Use

1. Run the script.
2. Enter two prime numbers (greater than or equal to 10).
3. Enter the message you want to encrypt.
4. The script will display the encrypted numeric message and then decrypt it back.

## Requirements

- Python 3.x
- Terminal or console that supports ANSI color codes (for colored output).

## Example
Enter a prime number p: 17
Enter a prime number q: 23
Enter a message to encrypt: Hello

Encrypted message: [some numbers]
Decrypted message: Hello

## Results
![image alt]([rsa_output.png](https://github.com/SanikaHegde/RSA-Encryption/blob/e9d01896e5fa8a8f009fc93bfe35a4e92e0e732c/rsa%20output.png))



