from typing import Optional
from algorithms import PuzzleState


def traverse_steps(state: Optional[PuzzleState]):
    if state is None:
        return
    traverse_steps(state.parent)
    print_step(state.grid, state.depth)


def print_step(step: list[int], i: int):
    print(f"Paso {i + 1}:")
    print(step[:3])
    print(step[3:6])
    print(step[6:])
    print()


def print_steps(final_state: PuzzleState):
    traverse_steps(final_state)

