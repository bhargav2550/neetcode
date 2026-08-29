
class FreqStack:

    def __init__(self):
        self.st = []
        self.ma = defaultdict(int)

    def push(self, val: int) -> None:
        self.st.append(val)
        self.ma[val] += 1

    def pop(self) -> int:
        x = max(self.ma.values())
        li = [i for i in self.ma if self.ma[i] == x]
        for i in range(len(self.st) - 1, -1, -1):
            if self.st[i] in li:
                self.ma[self.st[i]] -= 1
                x = self.st.pop(i)
                return x
        return -1


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()