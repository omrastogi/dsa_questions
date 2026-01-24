# rbtree.py
# Red–Black Tree implementation (CLRS-style) in Python 3
# Features:
# - search(key), insert(key), delete(key)
# - minimum(), maximum(), successor(node)
# - inorder(), preorder(), postorder() -> yields keys
# - validate() -> checks all RB invariants
# - pretty() -> ASCII visualization (small trees)
#
# Usage example at bottom.

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, Generator, Any

RED, BLACK = 0, 1

@dataclass
class Node:
    key: Any
    color: int = RED
    left: "Node" = None   # set after NIL is created
    right: "Node" = None
    parent: "Node" = None

    def __repr__(self):
        c = "R" if self.color == RED else "B"
        return f"{self.key}:{c}"

class RBTree:
    def __init__(self, iterable: Optional[Iterable[Any]] = None):
        self.NIL = Node(key=None, color=BLACK)
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL
        self.root: Node = self.NIL
        if iterable:
            for k in iterable:
                self.insert(k)

    # ---------- Utility ----------
    def _is_nil(self, x: Node) -> bool:
        return x is self.NIL

    def search_node(self, key: Any) -> Node:
        x = self.root
        while not self._is_nil(x) and key != x.key:
            x = x.left if key < x.key else x.right
        return x

    def search(self, key: Any) -> Optional[Any]:
        n = self.search_node(key)
        return None if self._is_nil(n) else n.key

    def minimum_node(self, x: Optional[Node] = None) -> Node:
        if x is None:
            x = self.root
        if self._is_nil(x):
            return self.NIL
        while not self._is_nil(x.left):
            x = x.left
        return x

    def maximum_node(self, x: Optional[Node] = None) -> Node:
        if x is None:
            x = self.root
        if self._is_nil(x):
            return self.NIL
        while not self._is_nil(x.right):
            x = x.right
        return x

    def minimum(self) -> Optional[Any]:
        n = self.minimum_node(self.root)
        return None if self._is_nil(n) else n.key

    def maximum(self) -> Optional[Any]:
        n = self.maximum_node(self.root)
        return None if self._is_nil(n) else n.key

    def successor(self, x: Node) -> Node:
        if not self._is_nil(x.right):
            return self.minimum_node(x.right)
        y = x.parent
        while not self._is_nil(y) and x is y.right:
            x = y
            y = y.parent
        return y

    # ---------- Rotations ----------
    def _left_rotate(self, x: Node) -> None:
        y = x.right
        if self._is_nil(y):
            return  # nothing to rotate
        x.right = y.left
        if not self._is_nil(y.left):
            y.left.parent = x
        y.parent = x.parent
        if self._is_nil(x.parent):
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y: Node) -> None:
        x = y.left
        if self._is_nil(x):
            return
        y.left = x.right
        if not self._is_nil(x.right):
            x.right.parent = y
        x.parent = y.parent
        if self._is_nil(y.parent):
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    # ---------- Insertion ----------
    def insert(self, key: Any) -> Node:
        z = Node(key=key, color=RED, left=self.NIL, right=self.NIL, parent=self.NIL)
        y = self.NIL
        x = self.root
        while not self._is_nil(x):
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if self._is_nil(y):
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self._insert_fixup(z)
        return z

    def _insert_fixup(self, z: Node) -> None:
        while z.parent.color == RED:
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right  # uncle
                if y.color == RED:
                    # Case 1
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        # Case 2
                        z = z.parent
                        self._left_rotate(z)
                    # Case 3
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)
        self.root.color = BLACK

    # ---------- Deletion ----------
    def _transplant(self, u: Node, v: Node) -> None:
        if self._is_nil(u.parent):
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_key(self, key: Any) -> bool:
        z = self.search_node(key)
        if self._is_nil(z):
            return False
        self.delete_node(z)
        return True

    def delete_node(self, z: Node) -> None:
        y = z
        y_original_color = y.color
        if self._is_nil(z.left):
            x = z.right
            self._transplant(z, z.right)
        elif self._is_nil(z.right):
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum_node(z.right)   # successor
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self._delete_fixup(x)

    def _delete_fixup(self, x: Node) -> None:
        while x is not self.root and x.color == BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    # Case 1
                    w.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    # Case 2
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        # Case 3
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = x.parent.right
                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    # ---------- Traversals ----------
    def inorder(self) -> Generator[Any, None, None]:
        def _in(n: Node):
            if self._is_nil(n): return
            yield from _in(n.left)
            yield n.key
            yield from _in(n.right)
        yield from _in(self.root)

    def preorder(self) -> Generator[Any, None, None]:
        def _pre(n: Node):
            if self._is_nil(n): return
            yield n.key
            yield from _pre(n.left)
            yield from _pre(n.right)
        yield from _pre(self.root)

    def postorder(self) -> Generator[Any, None, None]:
        def _post(n: Node):
            if self._is_nil(n): return
            yield from _post(n.left)
            yield from _post(n.right)
            yield n.key
        yield from _post(self.root)

    # ---------- Validators ----------
    def validate(self) -> bool:
        # 1) Root is black
        if not self._is_nil(self.root) and self.root.color != BLACK:
            return False
        # 2) NIL leaves are black: guaranteed by construction
        # 3) Red node has black children
        def no_red_red(n: Node) -> bool:
            if self._is_nil(n): return True
            if n.color == RED:
                if n.left.color != BLACK or n.right.color != BLACK:
                    return False
            return no_red_red(n.left) and no_red_red(n.right)
        if not no_red_red(self.root):
            return False
        # 4) BST order
        def is_bst(n: Node, lo, hi) -> bool:
            if self._is_nil(n): return True
            if (lo is not None and n.key <= lo) or (hi is not None and n.key >= hi):
                return False
            return is_bst(n.left, lo, n.key) and is_bst(n.right, n.key, hi)
        if not is_bst(self.root, None, None):
            return False
        # 5) Equal black-height on all root->leaf paths
        def black_height(n: Node) -> int:
            if self._is_nil(n):  # NIL counts as 1 black by CLRS convention
                return 1
            left_bh = black_height(n.left)
            right_bh = black_height(n.right)
            if left_bh == 0 or right_bh == 0 or left_bh != right_bh:
                return 0
            return left_bh + (1 if n.color == BLACK else 0)
        return black_height(self.root) > 0

    # ---------- Pretty print (for small trees) ----------
    def pretty(self) -> None:
        if self._is_nil(self.root):
            print("(empty)")
            return
        lines = []
        self._build_ascii(self.root, prefix="", is_left=False, out=lines)
        print("\n".join(lines))

    def _build_ascii(self, node: Node, prefix: str, is_left: bool, out: list[str]) -> None:
        if self._is_nil(node):
            return
        out.append(prefix + ("└── " if is_left else "┌── ") + repr(node))
        if not self._is_nil(node.left) or not self._is_nil(node.right):
            if not self._is_nil(node.right):
                self._build_ascii(node.right, prefix + ("    " if is_left else "│   "), False, out)
            if not self._is_nil(node.left):
                self._build_ascii(node.left, prefix + ("    " if is_left else "│   "), True, out)


# ---------------- Demo ----------------
if __name__ == "__main__":
    # Example usage
    keys = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    T = RBTree(keys)

    print("Inorder:", list(T.inorder()))
    print("Valid RB Tree?", T.validate())
    T.pretty()

    print("\nInsert 15")
    T.insert(15)
    print("Inorder:", list(T.inorder()))
    print("Valid RB Tree?", T.validate())

    print("\nDelete 18, 11, 3")
    for k in [18, 11, 3]:
        T.delete_key(k)
    print("Inorder:", list(T.inorder()))
    print("Min/Max:", T.minimum(), T.maximum())
    print("Valid RB Tree?", T.validate())
    T.pretty()

    # Search & successor demo
    node_10 = T.search_node(10)
    succ = T.successor(node_10)
    print("\nSuccessor of 10:", None if T._is_nil(succ) else succ.key)
