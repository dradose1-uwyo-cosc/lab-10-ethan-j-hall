# Ethan Hall
# UWYO COSC 1010
# 11.24.2024
# Lab XX
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

def get_hash(to_hash):
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

try:
    with open('hash', 'r') as file:
        target_hash = file.read().strip()  
except FileNotFoundError:
    print("The file 'hash' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the 'hash' file: {e}")
    exit()

try:
    with open('rockyou.txt', 'r', encoding='latin-1') as file:
        for password in file:
            password = password.strip()  
            if get_hash(password) == target_hash:
                print(f"Password found: {password}")
                break 
        else:
            print("Password not found in the list.")
except FileNotFoundError:
    print("The file 'rockyou.txt' was not found.")
except Exception as e:
    print(f"An error occurred while reading the 'rockyou.txt' file: {e}")
