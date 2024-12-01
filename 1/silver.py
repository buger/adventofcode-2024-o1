from collections import Counter
import sys

# Initialize lists
left_list = []
right_list = []

# Read input from stdin
for line in sys.stdin:
    if line.strip() == '':
        continue  # Skip empty lines
    parts = line.strip().split()
    if len(parts) != 2:
        continue  # Skip lines that don't have exactly two numbers
    left_num, right_num = map(int, parts)
    left_list.append(left_num)
    right_list.append(right_num)

# Count occurrences in the right list
right_counter = Counter(right_list)

# Calculate the similarity score
similarity_score = 0
for num in left_list:
    count_in_right = right_counter.get(num, 0)
    similarity_score += num * count_in_right

# Output the result
print(similarity_score)
