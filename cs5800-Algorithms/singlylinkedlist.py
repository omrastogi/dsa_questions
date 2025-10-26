class Node:
    __slots__ = ("val", "next")
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    """Simple singly linked list with standard operations."""
    __slots__ = ("_head", "_tail", "_size")

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # -------- utilities --------
    def __len__(self):
        return self._size

    def __repr__(self):
        return f"SinglyLinkedList({self.traverse()})"

    def _node_at(self, index: int) -> Node:
        if not (0 <= index < self._size):
            raise IndexError("index out of range")
        cur = self._head
        for _ in range(index):
            cur = cur.next
        return cur

    # -------- Traversal --------
    def traverse(self):
        """Return a Python list of all values."""
        out = []
        cur = self._head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

    # -------- Insertion --------
    def insert_begin(self, value):
        n = Node(value, self._head)
        self._head = n
        if self._tail is None:
            self._tail = n
        self._size += 1

    def insert_end(self, value):
        n = Node(value)
        if self._tail is None:
            self._head = self._tail = n
        else:
            self._tail.next = n
            self._tail = n
        self._size += 1

    def insert_at(self, index, value):
        """Insert at position [0..size]."""
        if not (0 <= index <= self._size):
            raise IndexError("index out of range")
        if index == 0:
            self.insert_begin(value)
            return
        if index == self._size:
            self.insert_end(value)
            return
        prev = self._node_at(index - 1)
        prev.next = Node(value, prev.next)
        self._size += 1

    # -------- Deletion --------
    def delete_begin(self):
        if self._head is None:
            raise IndexError("delete from empty list")
        n = self._head
        self._head = n.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return n.val

    def delete_end(self):
        if self._head is None:
            raise IndexError("delete from empty list")
        if self._head is self._tail:
            val = self._head.val
            self._head = self._tail = None
            self._size -= 1
            return val
        prev = self._head
        while prev.next is not self._tail:
            prev = prev.next
        val = self._tail.val
        prev.next = None
        self._tail = prev
        self._size -= 1
        return val

    def delete_at(self, index):
        if not (0 <= index < self._size):
            raise IndexError("index out of range")
        if index == 0:
            return self.delete_begin()
        prev = self._node_at(index - 1)
        target = prev.next
        prev.next = target.next
        if target is self._tail:
            self._tail = prev
        self._size -= 1
        return target.val

    # -------- Searching --------
    def search(self, key) -> bool:
        """Return True if key exists, else False."""
        cur = self._head
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    # (Optional helper if you want position)
    def find(self, key) -> int:
        """Return index of first occurrence or -1."""
        i, cur = 0, self._head
        while cur:
            if cur.val == key:
                return i
            cur = cur.next
            i += 1
        return -1

    # -------- Updating --------
    def update_at(self, index, new_value):
        self._node_at(index).val = new_value

    # -------- Reversal --------
    def reverse(self):
        """In-place reverse: make last node the new head."""
        prev = None
        cur = self._head
        self._tail = self._head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self._head = prev


if __name__ == "__main__":
    # Minimal runnable demo of the requested ops
    ll = SinglyLinkedList()

    # Insertion
    ll.insert_begin(20)     # [20]
    ll.insert_begin(10)     # [10, 20]
    ll.insert_end(30)       # [10, 20, 30]
    ll.insert_at(2, 25)     # [10, 20, 25, 30]
    print("After inserts:", ll)  # Traversal via __repr__

    # Searching
    print("search(25):", ll.search(25))  # True
    print("search(99):", ll.search(99))  # False

    # Updating
    ll.update_at(1, 21)    # [10, 21, 25, 30]
    print("After update_at(1,21):", ll.traverse())

    # Deletion
    print("delete_begin():", ll.delete_begin())  # removes 10
    print("delete_end():", ll.delete_end())      # removes 30
    print("delete_at(1):", ll.delete_at(1))      # removes 25
    print("Now:", ll.traverse())                 # [21]

    # Reversal
    ll.insert_end(40)       # [21, 40]
    ll.insert_end(50)       # [21, 40, 50]
    ll.reverse()            # [50, 40, 21]
    print("Reversed:", ll.traverse())
