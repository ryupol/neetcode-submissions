class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        min_val = val if not self.min_arr else min(self.min_arr[-1], val)
        self.min_arr.append(min_val)

    def pop(self) -> None:
        self.arr.pop()
        self.min_arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
