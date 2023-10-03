# Test email address 3
import re

email = input("what's your email?").strip()

if re.search(r".+@.+\.com", email):
    print("valid")
else:
    print("invalid")