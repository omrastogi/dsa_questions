from typing import Generic, Iterable, Iterator, List, Optional, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    """A simple LIFO stack implemented on top of Python's list."""

    __slots__ = ("_data",)

    def __init__(self, items: Optional[Iterable[T]] = None) -> None:
        self._data: List[T] = []
        if items:
            self._data.extend(items)

    # --- Core operations ---
    def push(self, item: T) -> None:
        """Push item onto the stack. Amortized O(1)."""
        self._data.append(item)

    def pop(self) -> T:
        """Remove and return the top item. Raises IndexError if empty."""
        return self._data.pop()

    def peek(self) -> T:
        """Return the top item without removing it. Raises IndexError if empty."""
        if not self._data:
            raise IndexError("peek from empty Stack")
        return self._data[-1]

    # --- Introspection / utilities ---
    def is_empty(self) -> bool:
        return not self._data

    def clear(self) -> None:
        self._data.clear()

    def size(self) -> int:
        return len(self._data)
    


if __name__ == "__main__":
    # 1) Basic push / peek / size
    s = Stack[int]()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top after pushes:", s.peek())   # 30
    print("Size:", s.size())               # 3
    print("Empty?:", s.is_empty())         # False

    # 2) Pop elements (LIFO)
    print("Pop:", s.pop())                 # 30
    print("Pop:", s.pop())                 # 20
    print("Top now:", s.peek())            # 10
    print("Size now:", s.size())           # 1

    # 3) Clear the stack
    s.clear()
    print("After clear, size:", s.size())  # 0
    print("Empty after clear?:", s.is_empty())  # True

    # 4) Construct with initial items (Iterable)
    s2 = Stack[str](items=["a", "b", "c"])
    print("Top s2:", s2.peek())            # c
    print("Size s2:", s2.size())           # 3

    # 5) Safe peek/pop pattern with empty-check
    if not s2.is_empty():
        print("Popped from s2:", s2.pop()) # c

    # 6) Demonstrate error on invalid peek/pop
    try:
        s.peek()                           # s is empty after clear()
    except IndexError as e:
        print("Expected error:", e)

    try:
        Stack().pop()                      # pop from empty
    except IndexError as e:
        print("Expected error:", e)
