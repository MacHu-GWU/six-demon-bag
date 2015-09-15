##encoding=utf-8

"""
bcrypt is a python extension to do modern password hashing for your software and your servers.
This script is to show you how to use bcrypt to verify users' login request.

Pypi homepage: https://pypi.python.org/pypi/bcrypt/2.0.0
Inside of cryptography algorithm: https://cryptography.io/en/latest/security/
"""

from __future__ import print_function
from __future__ import unicode_literals
import bcrypt

password = "super secret password".encode("utf-8")
hashed = bcrypt.hashpw(password, bcrypt.gensalt()) # you can use bcrypt.gensalt(rounds=14)
print(hashed)
print(bcrypt.hashpw(password, hashed))