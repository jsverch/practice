import copy

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        merged = list()
        for i in list(sorted(intervals, key=lambda i: i.start)):
            print "Doing [{}, {}]".format(i.start, i.end)
            for j in intervals:
                if i.start != j.start and i.end != j.end:
                    print "    Against [{}, {}]".format(j.start, j.end)
                    if i.start <= j.start < i.end or j.start <= i.start < j.end:
                        ni = Interval(min(i.start, j.start), max(i.end, j.end))
                        print "        Merged [{}, {}] + [{},{}] into [{}, {}]".format(i.start, i.end, j.start,
                                                                             j.end, ni.start, ni.end)
                        if j in intervals: intervals.remove(j)
                        if i in intervals: intervals.remove(i)
                        merged.append(ni)
                        # intervals.append(ni)
                        print "        Appended [{}, {}]".format(ni.start, ni.end)
                        break
        return merged


ivls = list()

ivls.append(Interval(2, 3))
ivls.append(Interval(1, 5))
ivls.append(Interval(6, 7))
ivls.append(Interval(8, 9))
ivls.append(Interval(1, 10))

s = Solution().merge(ivls)

for o in s:
    print ">  [{}, {}]".format(o.start, o.end)