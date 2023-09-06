
import random
import sys
import heapq

# Constants for game elements
RABBIT = 'r'
CARROT = 'c'
RABBIT_HOLE = 'O'
PATHWAY_STONE = '-'
HOLDING_CARROT = 'R'

# Define movements
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# function to generate a random map
def generate_map(size, num_carrots, num_holes):
    # Create an empty grid
    grid = [[PATHWAY_STONE] * size for _ in range(size)]

    # Place rabbit randomly
    rabbit_x, rabbit_y = random.randint(0, size - 1), random.randint(0, size - 1)
    grid[rabbit_y][rabbit_x] = RABBIT

    # Place carrots randomly
    for _ in range(num_carrots):
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        while grid[y][x] != PATHWAY_STONE:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[y][x] = CARROT

    # Place rabbit holes randomly
    for _ in range(num_holes):
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        while grid[y][x] != PATHWAY_STONE:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[y][x] = RABBIT_HOLE

    return grid, (rabbit_x, rabbit_y)

# function to display the game grid
def display_grid(grid):
    for row in grid:
        print(" ".join(row))

# Create a function to calculate the Manhattan distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Create a function to find the shortest path using A* algorithm
def find_shortest_path(grid, start, goal):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for dx, dy in MOVES:
            x, y = current[0] + dx, current[1] + dy

            if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] != PATHWAY_STONE:
                new_cost = cost_so_far[current] + 1

                if (x, y) not in cost_so_far or new_cost < cost_so_far[(x, y)]:
                    cost_so_far[(x, y)] = new_cost
                    priority = new_cost + manhattan_distance(goal, (x, y))
                    heapq.heappush(frontier, (priority, (x, y)))
                    came_from[(x, y)] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# play the game
def play_game(grid, rabbit_pos):
    rabbit_x, rabbit_y = rabbit_pos

    while True:
        display_grid(grid)
        action = input("Enter your move (w/a/s/d/p/j/Enter to show solution/q): ").lower()

        if action == 'q':
            print("Game over. You quit.")
            sys.exit()

        if action == '':
            # Show the solution
            show_solution(grid, rabbit_pos)
            return

        new_x, new_y = rabbit_x, rabbit_y

        if action == 'w':
            new_y -= 1
        elif action == 's':
            new_y += 1
        elif action == 'a':
            new_x -= 1
        elif action == 'd':
            new_x += 1
        elif action == 'j':
            if grid[rabbit_y][rabbit_x - 1] == RABBIT_HOLE:
                new_x -= 1
            elif grid[rabbit_y][rabbit_x + 1] == RABBIT_HOLE:
                new_x += 1
            elif grid[rabbit_y - 1][rabbit_x] == RABBIT_HOLE:
                new_y -= 1
            elif grid[rabbit_y + 1][rabbit_x] == RABBIT_HOLE:
                new_y += 1
        elif action == 'p':
            if grid[new_y][new_x] == CARROT:
                grid[new_y][new_x] = HOLDING_CARROT
                grid[rabbit_y][rabbit_x] = PATHWAY_STONE

        if grid[new_y][new_x] != PATHWAY_STONE and grid[new_y][new_x] != RABBIT_HOLE:
            print("Invalid move! Try again.")
        else:
            grid[new_y][new_x] = RABBIT if not HOLDING_CARROT else HOLDING_CARROT
            rabbit_x, rabbit_y = new_x, new_y

            if HOLDING_CARROT and grid[new_y][new_x] == RABBIT_HOLE:
                print("Congratulations! You won!")
                return

# Create a function to show the optimal solution
# ...

# Create a function to show the optimal solution
def show_solution(grid, rabbit_pos):
    rabbit_x, rabbit_y = rabbit_pos
    grid_copy = [row.copy() for row in grid]
    holding_carrot = False

    goal_positions = [(x, y) for y in range(len(grid_copy)) for x in range(len(grid_copy[y])) if grid_copy[y][x] == RABBIT_HOLE]

    for goal in goal_positions:
        path = find_shortest_path(grid_copy, (rabbit_x, rabbit_y), goal)
        for step in path:
            x, y = step
            if grid_copy[y][x] == CARROT:
                holding_carrot = True
            grid_copy[y][x] = RABBIT if not holding_carrot else HOLDING_CARROT
            display_grid(grid_copy)
            input("Press Enter to continue...")

if __name__ == "__main__":
    size = int(input("Enter the size of the grid: "))
    num_carrots = int(input("Enter the number of carrots: "))
    num_holes = int(input("Enter the number of rabbit holes: "))

    grid, rabbit_pos = generate_map(size, num_carrots, num_holes)
    print("Instructions:")
    print("Press Enter to play the game; Press any other key to quit.")
    while True:
        action = input()
        if action == '':
            play_game(grid, rabbit_pos)
