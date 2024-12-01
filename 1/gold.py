# Read input from standard input
import sys

left_list = []
right_list = []

for line in sys.stdin:
    if line.strip() == '':
        continue  # skip empty lines
    parts = line.strip().split()
    if len(parts) != 2:
        continue  # skip lines that don't have exactly two numbers
    left_num, right_num = map(int, parts)
    left_list.append(left_num)
    right_list.append(right_num)

# Sort both lists
left_list.sort()
right_list.sort()

# Compute the sum of absolute differences
total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))

# Print the result
print(total_distance)
