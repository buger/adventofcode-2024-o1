def is_safe(levels):
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    # Check that no differences are zero
    if any(d == 0 for d in differences):
        return False
    # Check that all differences are between 1 and 3 inclusive in absolute value
    if not all(1 <= abs(d) <= 3 for d in differences):
        return False
    # Check if all increasing or all decreasing
    if all(d > 0 for d in differences) or all(d < 0 for d in differences):
        return True
    else:
        return False

safe_reports = 0

# Read input data
import sys

for line in sys.stdin:
    levels = list(map(int, line.strip().split()))
    if levels and is_safe(levels):
        safe_reports += 1

print(safe_reports)
