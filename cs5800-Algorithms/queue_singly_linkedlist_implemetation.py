class Node:
    __slots__ = ("val", "next")
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:

    __slots__ = ("_head", "_tail", "_size")
    
    def __init__(self):
        self._tail = None 
        self._head = None
        self._size = 0

    def enqueue(self, val):
        if self._tail:
            self._tail.next = Node(val=val)
            self._tail = self._tail.next
        else:
            self._head = self._tail = Node(val)
        self._size += 1
        # No overflow condition exist 
    
    def dequeue(self):
        if self._head == None:
            raise Exception("Queue Underflow")
        val = self._head.val
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
        self._size -= 1
        return val

    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"Queue({self.traverse()})"

    def traverse(self):
        """Return a Python list of all values."""
        out = []
        cur = self._head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out
        

if __name__ == "__main__":
    # Minimal runnable demo of the requested ops
    que = Queue()

    # Insertion
    que.enqueue(20)     # [20]
    print("After enqueues:", que)  # Traversal via __repr__
    que.enqueue(10)     # [10, 20]
    print("After enqueues:", que)  # Traversal via __repr__
    que.enqueue(30)     # [10, 20, 30]
    print("After enqueues:", que)  # Traversal via __repr__
    que.dequeue()
    print("After dequeue:", que)   # Traversal via __repr__
    que.dequeue()
    print("After dequeue:", que)
    que.dequeue()
    print("After dequeue:", que)

