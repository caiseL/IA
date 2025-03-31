import heapq
from typing import Optional

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = {
    "U": -3,  # Move up
    "D": 3,  # Move down
    "L": -1,  # Move left
    "R": 1,  # Move right
}


# Heuristic function for A* algorithm. Manhattan distance is used as the heuristic.
def heuristic(grid: list[int]):
    distance = 0
    for i in range(9):
        grid_element = grid[i]
        if grid_element != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(grid_element - 1, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


class PuzzleState:
    def __init__(
        self,
        grid: list[int],
        parent: Optional["PuzzleState"],
        heuristic: int,
        depth: int,
    ):
        self.grid = grid
        self.parent = parent
        self.heuristic = heuristic
        self.depth = depth

    def __lt__(self, other: "PuzzleState"):
        return self.heuristic < other.heuristic


def a_star(start: list[int]) -> PuzzleState:
    closed_list = set()

    open_list: list[PuzzleState] = []
    heapq.heappush(open_list, PuzzleState(start, None, heuristic(start), 0))

    while open_list:
        current = heapq.heappop(open_list)
        if current.grid == goal:
            return current

        closed_list.add(tuple(current.grid))

        blank_position = current.grid.index(0)
        for move in moves:
            if (
                move == "U"
                and blank_position < 3
                or move == "D"
                and blank_position > 5
                or move == "L"
                and blank_position % 3 == 0
                or move == "R"
                and blank_position % 3 == 2
            ):
                continue

            new_grid = current.grid.copy()
            new_blank_position = blank_position + moves[move]
            new_grid[blank_position], new_grid[new_blank_position] = (
                new_grid[new_blank_position],
                new_grid[blank_position],
            )

            if tuple(new_grid) in closed_list:
                continue

            new_state = PuzzleState(
                new_grid,
                current,
                current.heuristic + 1 + heuristic(new_grid),
                current.depth + 1,
            )
            heapq.heappush(open_list, new_state)

    raise ValueError("No solution found")
