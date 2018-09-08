# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#

import json


class Solution:
  def evalRPN(self, tokens):
    stack = []
    for token in tokens:
      if token in '+*-/':
        a, b = stack.pop(), stack.pop()
        if token == '+':
          stack.append(a + b)
        if token == '*':
          stack.append(a * b)
        if token == '-':
          stack.append(b - a)
        if token == '/':
          stack.append(int(b / a))
        continue
      stack.append(int(token))
    return stack.pop()


def stringToStringArray(input):
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
            tokens = stringToStringArray(line)
            ret = Solution().evalRPN(tokens)
            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()