class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = list()
        stack = path.split('/')
        for e in stack:
            print('e:{}'.format(e))
            if e == "." or '':
                pass
            elif e == "..":
                answer.pop()
            elif e != "":
                answer.append(e)
        print('answer:{}'.format(answer))
        simple = ' '.join(answer).split()
        return '/'+'/'.join(simple)



obj = Solution()

path = "/a//b////c/d//././/.."

print(obj.simplifyPath(path))

