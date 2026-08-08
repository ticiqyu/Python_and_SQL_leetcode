class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.a = []       
        self.mul = 1      
        self.add = 0      

    def append(self, val: int) -> None:
        # Сохраняем val таким, чтобы val == (x * mul + add) % MOD
        # x = (val - add) / mul  =>  x = (val - add) * inv(mul)
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        raw = ((val - self.add) * inv_mul) % self.MOD
        self.a.append(raw)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.a):
            return -1
        return (self.a[idx] * self.mul + self.add) % self.MOD

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)