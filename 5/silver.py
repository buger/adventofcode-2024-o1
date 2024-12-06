import sys
from collections import defaultdict, deque

def main():
    lines = sys.stdin.read().splitlines()
    # Split input into ordering rules and updates
    idx = lines.index('')
    ordering_rules_lines = lines[:idx]
    updates_lines = lines[idx+1:]

    # Parse the ordering rules
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
        if not correct:
            # Reorder the update using topological sort
            # Build the graph
            graph = defaultdict(list)
            in_degree = defaultdict(int)
            nodes_in_update = set(update_pages)
            for page in nodes_in_update:
                in_degree[page] = 0  # Initialize in-degree

            for X, Y in ordering_rules:
                if X in nodes_in_update and Y in nodes_in_update:
                    graph[X].append(Y)
                    in_degree[Y] += 1

            # Perform topological sort
            # Initialize the queue with nodes of in-degree zero
            queue = deque()
            page_order = []
            # For determinism, use the order from the original update
            for page in update_pages:
                if in_degree[page] == 0:
                    queue.append(page)

            while queue:
                page = queue.popleft()
                page_order.append(page)
                for neighbor in graph[page]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if len(page_order) != len(nodes_in_update):
                print("Cycle detected, cannot perform topological sort.")
                continue  # Skip this update

            # Extract the middle page number
            middle_page = page_order[len(page_order)//2]
            total += middle_page

    print(total)

if __name__ == "__main__":
    main()
