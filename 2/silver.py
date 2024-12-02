import sys

def is_safe_sequence(levels):
    """
    Checks if the sequence is strictly increasing or decreasing
    with acceptable differences (<= 3 in absolute value).
    """
    if len(levels) < 2:
        return True  # A single level is considered safe

    # Check for increasing sequence
    is_increasing = True
    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]
        if diff <= 0 or abs(diff) > 3:
            is_increasing = False
            break

    if is_increasing:
        return True

    # Check for decreasing sequence
    is_decreasing = True
    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]
        if diff >= 0 or abs(diff) > 3:
            is_decreasing = False
            break

    return is_decreasing

def can_be_made_safe(levels):
    """
    Checks if the sequence can be made safe by removing at most one level.
    """
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe_sequence(new_levels):
            return True
    return False

def main():
    reports = []

    # Read reports from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        levels = list(map(int, line.split()))
        reports.append(levels)

    safe_reports = 0

    for levels in reports:
        if is_safe_sequence(levels):
            safe_reports += 1
        elif can_be_made_safe(levels):
            safe_reports += 1

    print(safe_reports)

if __name__ == "__main__":
    main()
