from bst import BinarySearchTree


def main():
    bst = BinarySearchTree[int]()

    # Insert 10 numbers in the tree
    [bst.insert(x) for x in range(10, 0, -1)]

    print("Números en el arbol: ")
    bst.print()

    num_to_search = 0
    print(f"Buscando el número {num_to_search} en el árbol")
    print(
        f"El número {num_to_search} {'sí' if bst.search(num_to_search) else 'no'} está en el árbol"
    )


if __name__ == "__main__":
    main()
