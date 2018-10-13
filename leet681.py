class Solution(object):
    def tDiff(self, target, comb):
        diff = 0
        if comb < target:
            diff += 2400
        diff += (comb - target)
        # print "T:{} C:{} D:{}".format(target, comb, diff)
        return diff

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = list(time)
        nums.remove(":")
        target = int(time.replace(':', ''))
        combs = dict()

        # print nums
        h1 = [i for i in nums if int(i) < 3]
        h2 = [i for i in nums]
        m1 = [i for i in nums if int(i) < 6]
        m2 = [i for i in nums]

        for a in h1:
            for b in h2:
                for c in m1:
                    for d in m2:
                        cm = int(a+b+c+d)
                        if cm > 2401:
                            break
                        else:
                            dif = self.tDiff(target, int(a+b+c+d))
                        if dif:
                            # print "{} - {}".format(a+b+c+d, dif)
                            combs[a+b+c+d] = dif
        if len(combs):
            # print combs
            n = str(min(combs, key=combs.get))
            return n[:2]+":"+n[2:]
        else:
            return time


print Solution().nextClosestTime("00:00")
