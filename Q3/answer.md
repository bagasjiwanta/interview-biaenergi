# Question #3 (algorithm)

The following class describes a node on a binary tree. A node can have a left child, or a right child, or both, or no child at all.

CODE:

```py
class Node:
    def __init__(self):
        self.right = None
        self.left = None
```

QUESTION:

Write the content of the method below that counts the maximum number of levels in a given tree. Please notice that this is NOT counting the TOTAL number of nodes, but counting the DEPTH.

```py
def calculateMaxDepth(n):
    if n is None:
        return 0
    return 1 + max(
        calculateMaxDepth(n.left),
        calculateMaxDepth(n.right)
    )
```

Answer:

```py
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
```
