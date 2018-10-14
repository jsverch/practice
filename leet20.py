class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        sl = list(s)
        stack = list()
        opens = ['(', '[', '{']

        for c in sl:
            print c
            if c in opens:
                stack.append(c)
            else: #closer
                if not len(stack):
                    return False
                e = stack.pop()
                if e == "(" and c != ")":
                    return False
                elif e == "{" and c != "}":
                    return False
                elif e == "[" and c != "]":
                    return False

        if len(stack) != 0:
            return False
        else:
            return True


print Solution().isValid("([)]")
