# Random Password Generator

A simple command-line tool that generates a secure, random password of a length you choose, using Python's `secrets` module for cryptographically strong randomness.

## Features
- Generates random passwords using letters (upper + lower case) and digits
- Uses the `secrets` module for secure randomness (safer than `random`)
- Validates input to ensure a positive whole number is entered

## Requirements
- Python 3.12+ (tested on 3.12.1)
- No external libraries needed (`secrets` and `string` are part of the standard library)

## How to Run
```bash
python password_generator.py
```

## Usage
1. Run the script.
2. Enter the desired password length when prompted.
3. Get your randomly generated password.

## Example
```
=== Random Password Generator ===
Enter the desired password length: 12

Generated Password: aZ3kLm9QpX2r
```

