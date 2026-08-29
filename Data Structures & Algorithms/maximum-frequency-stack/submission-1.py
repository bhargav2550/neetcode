
class FreqStack:

    def __init__(self):
        self.maxCnt = 1
        self.cnt = defaultdict(int)
        self.stacks = {}

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        currCnt = self.cnt[val]
        self.maxCnt = max(currCnt, self.maxCnt)
        if currCnt not in self.stacks:
            self.stacks[currCnt] = [val]
        else:
            self.stacks[currCnt].append(val)


    def pop(self) -> int:
        ans = self.stacks[self.maxCnt].pop()
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        self.cnt[ans] -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()