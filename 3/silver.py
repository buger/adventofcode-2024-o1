import re
import sys

# Read input from stdin
input_string = sys.stdin.read()

# Define the regex pattern
pattern = r"(?P<mul>mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\))|(?P<do>do\(\))|(?P<dont>don't\(\))"

total = 0
enabled = True

# Iterate over all matches in the input string
for match in re.finditer(pattern, input_string):
    if match.group('do'):
        enabled = True
    elif match.group('dont'):
        enabled = False
    elif match.group('mul') and enabled:
        a = int(match.group('a'))
        b = int(match.group('b'))
        total += a * b

# Output the total sum
print(total)
