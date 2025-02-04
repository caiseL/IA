from typing import Generic, Optional, Self, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    left: Optional[Self]
    right: Optional[Self]
    value: T

    def __init__(self, value: T) -> None:
        self.left = self.right = None
        self.value = value


class BinarySearchTree(Generic[T]):
    root: Optional[Node[T]]

    def __init__(self) -> None:
        self.root = None

    def search(self, value: T) -> bool:
        def __search_node(node: Optional[Node[T]], value: T) -> bool:
            if node is None:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return __search_node(node.left, value)
            return __search_node(node.right, value)

        return __search_node(self.root, value)

    def insert(self, value: T):
        def __insert_node(node: Node[T], value: T):
            if value <= node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                __insert_node(node.left, value)
                return
            if node.right is None:
                node.right = Node(value)
                return
            __insert_node(node.right, value)

        if self.root is None:
            self.root = Node[T](value)
            return
        return __insert_node(self.root, value)

    def print(self):
        def __print(node: Optional[Node[T]]):
            if node is None:
                return
            __print(node.left)
            print(node.value)
            __print(node.right)

        __print(self.root)
