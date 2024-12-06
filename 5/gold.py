import sys

def main():
    lines = sys.stdin.read().splitlines()
    # Split input into ordering rules and updates
    idx = lines.index('')
    ordering_rules_lines = lines[:idx]
    updates_lines = lines[idx+1:]

    ordering_rules = []
    for line in ordering_rules_lines:
        X, Y = map(int, line.strip().split('|'))
        ordering_rules.append((X, Y))

    total = 0
    for update_line in updates_lines:
        update_pages = list(map(int, update_line.strip().split(',')))
        page_to_index = {page: idx for idx, page in enumerate(update_pages)}
        correct = True
        for X, Y in ordering_rules:
            if X in page_to_index and Y in page_to_index:
                if page_to_index[X] >= page_to_index[Y]:
                    correct = False
                    break
        if correct:
            middle_page = update_pages[len(update_pages)//2]
            total += middle_page

    print(total)

if __name__ == "__main__":
    main()
