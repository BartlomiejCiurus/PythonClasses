CURRENT_LEAF = 1
EMPTY_TREE = 0


class Leaf:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def count_total(top):
    if top is None:
        return EMPTY_TREE
    return count_total(top.left) + top.value + count_total(top.right)


def count_leafs(top):
    if top is None:
        return EMPTY_TREE
    if top.left is None and top.right is None:
        return count_leafs(top.left) + CURRENT_LEAF + count_leafs(top.right)
    else:
        return count_leafs(top.left) + count_leafs(top.right)
