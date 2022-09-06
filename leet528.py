import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        # print("Weighting: {}".format(w))
        s = sum(w)
        self.weights = dict()
        i = 0
        for e in w:
            cw = e/s
            # print("index {} gets weight {}".format(i,cw))
            self.weights[i] = cw
            i += 1
        # print(self.weights)
        self.sw = dict(sorted(self.weights.items(), key=lambda item: item[1]))
        # print(self.sw)

    def pickIndex(self) -> int:
        r = random.random()
        print("random:{}".format(r))
        vs = list(self.sw.values())
        i = 0
        for v in self.sw.values():
            if i < len(vs) - 1:
                # print("v:{}, v+1:{}".format(v, vs[i + 1]))
                if r >= v and r < vs[i + 1]:
                    return(i)
                i += 1
            else:
                return(i)



w = [3, 14, 1, 7]
# w = [1]
obj = Solution(w)

param_1 = obj.pickIndex()
print(param_1)
