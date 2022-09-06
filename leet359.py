class Logger:

    def __init__(self):
        self.messages = dict()

    def shouldPrintMessage(self, t: int, m: str) -> bool:
        if m not in self.messages.keys():
            self.messages[m] = t
            return True
        elif t - self.messages[m] < 10:
            return False
        else:
            self.messages[m] = t
            return True

# Your Logger object will be instantiated and called as such:
obj = Logger()
p = list()

t1 = 1
m1 = "foo"
p.append(obj.shouldPrintMessage(t1, m1))

t2 = 2
m2 = "bar"
p.append(obj.shouldPrintMessage(t2, m2))

t3 = 3
m3 = "foo"
p.append(obj.shouldPrintMessage(t3, m3))

t4 = 8
m4 = "bar"
p.append(obj.shouldPrintMessage(t4, m4))

t5 = 10
m5 = "foo"
p.append(obj.shouldPrintMessage(t5, m5))

t6 = 11
m6 = "foo"
p.append(obj.shouldPrintMessage(t6, m6))

print(p)