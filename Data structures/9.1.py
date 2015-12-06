def remove_head(node):
    node.value = node.next_node
    node.next_node = node.next_node.next_node
    return Node(node.value, node.next_node)


def remove_tail(node):
    current_node = node
    tail = None
    one_before_tail = None
    while current_node:
        one_before_tail = tail
        tail = current_node
        current_node = current_node.next_node
    tail.next_node = None
    tail.value = None
    one_before_tail.next_node = None
    return Node(one_before_tail.value, one_before_tail.next_node)


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
