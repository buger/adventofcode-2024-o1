import re
import sys

# Read input from stdin
input_string = sys.stdin.read()

# Find all valid mul instructions
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_string)

# Sum the results of the multiplications
total = sum(int(x) * int(y) for x, y in matches)

print(total)
