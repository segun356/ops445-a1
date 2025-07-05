#!/usr/bin/env python3

import sys

if len(sys.argv) != 4:
    print("Usage: ./a1.py num1 num2 num3")
    exit(1)

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])
except ValueError:
    print("All arguments must be integers.")
    exit(1)

highest = max(num1, num2, num3)
lowest = min(num1, num2, num3)
difference = highest - lowest

print("highest:", highest)
print("lowest:", lowest)
print("range:", difference)
