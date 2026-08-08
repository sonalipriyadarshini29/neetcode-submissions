class MyHashSet:

    def __init__(self):
        self.data = set()

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.add(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        else:
            self.data = self.data

    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)