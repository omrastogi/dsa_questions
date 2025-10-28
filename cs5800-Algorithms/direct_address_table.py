# Reference: https://www.geeksforgeeks.org/java/java-program-to-implement-direct-addressing-tables/

class Student:
    def __init__(self, rollnum, name, age):
        self.key = self.rollnumber = rollnum
        self.name = name 
        self.age = age

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}(rollnumber={self.rollnumber!r}, name={self.name!r}, age={self.age!r})"
 

class DirectAddressTables:
    def __init__(self, k=10):
        self.table = [None]*k
    
    def search(self, i):
        return self.table[i]
    
    def insert(self, x):
        self.table[x.key] = x
    
    def delete(self, x):
        self.table[x.key] = None

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self.table})"
    

if __name__=="__main__":
    table = DirectAddressTables(k=100)
    table.insert(Student(12, "Huma", 15))
    table.insert(Student(15, "Numma", 15))
    print(table.search(12))
    print(table)


