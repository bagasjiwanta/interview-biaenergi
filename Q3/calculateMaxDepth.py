import unittest


class Node:
    def __init__(self):
        self.right = None
        self.left = None


def generate_test_tree():
    root = Node()
    root.left = Node()
    root.right = Node()
    root.right.right = Node()
    return root


def isEmpty(n: Node) -> bool:
    return n is None


def calculateMaxDepth(n: Node) -> int:
    # base case
    if isEmpty(n):
        return 0

    # depth is the greater depth from left and right child
    return 1 + max(
        calculateMaxDepth(n.left),
        calculateMaxDepth(n.right)
    )


class TestTree(unittest.TestCase):
    def test_depth(self):
        tree = generate_test_tree()
        self.assertEqual(calculateMaxDepth(tree), 3)


if __name__ == '__main__':
    unittest.main()
