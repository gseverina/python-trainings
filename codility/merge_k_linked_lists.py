# from Real Python - Hard Interview Question
class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"

    def __eq__(self, other):
        if self.val != other.val:
            return False
        else:
            return self.next == other.next

        return False

    def add(self, node):
        if node.val < self.val:
            aux = Link(self.val, self.next)
            self.val = node.val
            if node.next:
                node.next.add(aux)
                self.next = node.next
            else:
                self.next = aux
        else:
            if self.next:
                self.next.add(node)
            else:
                self.next = node


def merge_k_linked_lists(linked_lists):
    """
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    """
    for i in range(1, len(linked_lists)):
        linked_lists[0].add(linked_lists[i])
    return linked_lists[0]


if __name__ == "__main__":
    # lst = [Link(2), Link(1)]
    # for x in lst:
    #     print(f"Original: {x}")
    # print(f"Merged: {merge_k_linked_lists(lst)}")

    # lst = [Link(1), Link(2)]
    # for x in lst:
    #     print(f"Original: {x}")
    # print(f"Merged: {merge_k_linked_lists(lst)}")
    #
    # lst = [Link(1, Link(2)), Link(3, Link(4))]
    # for x in lst:
    #     print(f"Original: {x}")
    # print(f"Merged: {merge_k_linked_lists(lst)}")

    lst = [Link(1, Link(2)), Link(2, Link(4)), Link(3, Link(3))]
    for x in lst:
        print(f"Original: {x}")
    print(f"Merged: {merge_k_linked_lists(lst)}")
