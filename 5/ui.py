def print_steps(steps):
    for i, step in enumerate(steps):
        print(f"Paso {i}:")
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()