def remove_head(node):
    if node is None:
        raise ValueError
    temp = node
    wart = node.data
    node = node.next
    del temp
    return node, wart


def remove_tail(node):
    if node is None:
        raise ValueError
    elif node.next is None:
        wart = node.data
        del node
        return None, wart
    else:
        previous = node
        actual = node.next
        while actual.next:
            previous, actual = actual, actual.next
        wart = actual.data
        del actual
        previous.next = None
        return node, wart


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
