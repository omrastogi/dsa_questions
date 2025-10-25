from typing import Generic, Iterable, Optional, TypeVar
from stack import Stack 

T = TypeVar("T")


class Queue(Generic[T]):
    """FIFO queue implemented using two Stacks."""

    __slots__ = ("_in", "_out")

    def __init__(self, items: Optional[Iterable[T]] = None) -> None:
        self._in: Stack[T] = Stack()
        self._out: Stack[T] = Stack()
        if items:
            for x in items:        # enqueue in given order
                self.enqueue(x)

    # --- Core operations ---
    def enqueue(self, item: T) -> None:
        """Add item to the back of the queue. Amortized O(1)."""
        self._in.push(item)

    def _fill_out(self) -> None:
        """Move all elements from _in to _out if _out is empty."""
        if self._out.is_empty():
            while not self._in.is_empty():
                self._out.push(self._in.pop())

    def dequeue(self) -> T:
        """Remove and return the front item. Raises IndexError if empty."""
        self._fill_out()
        return self._out.pop()  # may raise IndexError if empty

    def front(self) -> T:
        """Return the front item without removing it. Raises IndexError if empty."""
        self._fill_out()
        return self._out.peek()

    # --- Introspection / utilities ---
    def is_empty(self) -> bool:
        return self._in.is_empty() and self._out.is_empty()

    def size(self) -> int:
        return self._in.size() + self._out.size()

    def clear(self) -> None:
        self._in.clear()
        self._out.clear()

    # --- Python protocol methods ---
    def __len__(self) -> int:
        return self.size()

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __repr__(self) -> str:
        # Build a readable snapshot without mutating stacks
        # Items currently in _out are in correct front->back order (top of _out is front).
        # Items in _in are in reverse order (top is newest); we show logical order.
        out_list = []
        tmp = Stack[T]()
        # Peek through _out (front part)
        while not self._out.is_empty():
            v = self._out.pop()
            out_list.append(v)
            tmp.push(v)
        while not tmp.is_empty():
            self._out.push(tmp.pop())
        # Collect _in (back part) in enqueue order
        in_list = []
        while not self._in.is_empty():
            v = self._in.pop()
            tmp.push(v)
        while not tmp.is_empty():
            v = tmp.pop()
            self._in.push(v)
            in_list.append(v)
        logical = list(reversed(out_list)) + in_list  # front -> back
        return f"Queue({logical!r})"

if __name__ == "__main__":
    q = Queue[int]([1, 2, 3])
    print("Initial:", q)                # Queue([1, 2, 3])
    q.enqueue(4)
    q.enqueue(5)
    print("After enqueue 4,5:", q)     # Queue([1, 2, 3, 4, 5])

    print("Front:", q.front())         # 1
    print("Dequeue:", q.dequeue())     # 1
    print("After one dequeue:", q)     # Queue([2, 3, 4, 5])

    # Interleave to test the two-stack behavior
    q.enqueue(6)
    q.enqueue(7)
    print("After enqueue 6,7:", q)     # Queue([2, 3, 4, 5, 6, 7])

    while q:
        print("pop ->", q.dequeue())
