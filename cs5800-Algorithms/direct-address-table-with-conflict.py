# Assumption: Students are from different sections, hence the rollnumber can collide 
# We use the rollnumber as keys // Reference: https://github.com/omrastogi/dsa_questions/blob/master/cs5800-Algorithms/direct_address_table.py
class Student:
    def __init__(
            self, 
            rollnum, 
            name, 
            age, 
            section="A"):
        self.key = self.rollnumber = rollnum
        self.name = name 
        self.age = age
        self.section = section

    def __repr__(self):
        cls = self.__class__.__name__
        return (f"{cls}("
            f"rollnumber={self.rollnumber!r}, "
            f"name={self.name!r}, "
            f"age={self.age!r}, "
            f"section={self.section!r})")


class Node:
    def __init__(
            self, 
            prev=None, 
            next=None,
            obj=None):
        self.prev = prev
        self.val = obj 
        self.next = next 
    
    def __repr__(self):
        cls = self.__class__.__name__
        prev_id = id(self.prev) if self.prev else None
        return f"{cls}(prev={prev_id!r}, object={self.val!r}, next={self.next!r})"

class DirectAddressTables:
    def __init__(self, k=10):
        self.table = [None]*k
    
    def search(self, key):
        """Return a list of all students stored under this key."""
        results = []
        node = self.table[key]
        return node
    
    def insert(self, x):
        key = x.key
        new_node = Node(obj=x)

        # If slot is empty, directly insert
        if self.table[key] is None:
            self.table[key] = new_node
        else:
            # Insert at the end of the doubly linked list
            curr = self.table[key]
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    def delete(self, x):
        """Delete the node containing object x."""
        key = x.val.key
        if x.prev is None:
            self.table[key] = x.next
            if x.next:
                x.next.prev = None

        elif x.next is None:
            x.prev.next = None
        else:
            x.next.prev, x.prev.next = x.prev, x.next
        
        x.next = x.prev = None
        del x 
        return self.search(key)

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self.table})"

if __name__=="__main__":
    table = DirectAddressTables(k=20)
    table.insert(Student(12, "Huma", 15, "A"))
    table.insert(Student(12, "Yashi", 16, "B"))
    table.insert(Student(12, "Aman", 13, "C"))
    print(table.search(12))
    p = table.search(12).next
    print(table.delete(p))
