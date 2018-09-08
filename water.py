import json


class Solution(object):
    def trap(self, height):
        r, redge = len(height) - 1, len(height) - 1
        l, ledge = 0, 0
        ans = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if height[l] < height[ledge]:
                    ans += height[ledge] - height[l]
                else:
                    ledge = l
            else:
                r -= 1
                if height[r] < height[redge]:
                    ans += height[redge] - height[r]
                else:
                    redge = r
        return ans


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            height = stringToIntegerList(line)
            ret = Solution().trap(height)
            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()