# import unittest


class NumStack:
    def __init__(self):
        self.ostack = list()
        self.hstack = list()
        self.lstack = list()
        self.total = float()

    def push(self, v):
        h_i, l_i = False, False
        if not isinstance(v, (int, float, float)):
            raise ValueError("Can only push int, float, or long.")
        self.ostack.append(v)
        self.total += v
        if len(self.hstack) == 0:
            self.hstack.append(v)
            h_i = True
        if len(self.lstack) == 0:
            self.lstack.append(v)
            l_i = True
        if not h_i:
            if v >= self.hstack[len(self.hstack) - 1]:
                self.hstack.append(v)
        if not l_i:
            if v <= self.lstack[len(self.lstack) - 1]:
                self.lstack.append(v)

    def size(self):
        return len(self.ostack)

    def pop(self):
        v = self.ostack.pop()
        if v == self.hstack[len(self.hstack) - 1]:
            self.hstack.pop()
        if v == self.lstack[len(self.lstack) - 1]:
            self.lstack.pop()
        return v

    def max(self):
        return self.hstack[len(self.hstack) - 1]

    def min(self):
        return self.lstack[len(self.lstack) - 1]

    def avg(self):
        return self.total / float(self.size())


# class NumStackTest(unittest.TestCase):
#     def test_push_pop(self):
#         n1 = NumStack()
#         n1.push(42.0)
#         self.assertEquals(n1.pop(), 42.0, "Didn't pop what we pushed")
#
#     def test_avg(self):
#         n2 = NumStack()
#         n2.push(10)
#         n2.push(14)
#         n2.push(20)
#         n2.push(11)
#         n2.push(8)
#         self.assertEqual(n2.avg(), 12.6, "Average was wrong")


# unittest.main()
#
# exit()


n = NumStack()

n.push(5)
n.push(3.0)
n.push(8)
n.push(1)
n.push(3)
n.push(3)

print("Length : {}\nMin : {}\nMax : {}\nAvg : {}".format(n.size(), n.min(), n.max(), n.avg()))

print("Pop : {}".format(n.pop()))
print("Pop : {}".format(n.pop()))
print("Pop : {}".format(n.pop()))

n.push(-4)


print("Max : {}".format(n.max()))
print("Min : {}".format(n.min()))