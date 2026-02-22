from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    if target > max(jug1_capacity, jug2_capacity):
        return "No solution possible"

    visited = set()
    queue = deque()
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        if jug1 == target or jug2 == target:
            path.append((jug1, jug2))
            return path

        next_states = []

        next_states.append((jug1_capacity, jug2))
        next_states.append((jug1, jug2_capacity))
        next_states.append((0, jug2))
        next_states.append((jug1, 0))

        transfer = min(jug1, jug2_capacity - jug2)
        next_states.append((jug1 - transfer, jug2 + transfer))

        transfer = min(jug2, jug1_capacity - jug1)
        next_states.append((jug1 + transfer, jug2 - transfer))

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path + [(jug1, jug2)]))

    return "No solution found"


jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug_problem(jug1, jug2, target)

if isinstance(solution, list):
    print("Solution Steps:")
    for step in solution:
        print(step)
else:
    print(solution)


output :
Enter capacity of Jug 1: 4
Enter capacity of Jug 2: 3
Enter target amount: 2

Solution Steps:
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2)
