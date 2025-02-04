from bst import BinarySearchTree


def main():
    bst = BinarySearchTree[int]()
    bst.insert(1)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)

    bst.print()


if __name__ == "__main__":
    main()
