from algorithms import a_star
from ui import print_steps


def main():
    initial = [2, 1, 3, 4, 5, 6, 7, 8, 0]
    steps = a_star(initial)
    print_steps(steps)


if __name__ == "__main__":
    main()
