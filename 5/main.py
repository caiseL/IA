from algorithms import a_star
from ui import print_steps


def main():
    initial = [8, 6, 7, 2, 5, 4, 3, 0, 1]

    try:
        final_state = a_star(initial)
        print_steps(final_state)
    except ValueError as e:
        print(e)
        return


if __name__ == "__main__":
    main()

