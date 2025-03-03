from algorithms import a_star
from ui import print_steps

def main():
    initial = [8, 6, 7, 2, 5, 4, 3, 0, 1]
    steps = a_star(initial)

    if steps:
        print("Solución encontrada:")
        print_steps(steps)
    else:
        print("No hay solución para este estado inicial.")

if __name__ == "__main__":
    main()