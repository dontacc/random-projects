class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def to_string(self):
        node = self.head
        while (node is not None):
            print(node.value)
            node = node.next


def main():
    node1 = Node(value=1)
    node2 = Node(value="arian")
    node3 = Node(value="jack")

    node1.next = node2
    node2.next = node3

    linked = LinkedList(head=node1)
    linked.to_string()


main()
