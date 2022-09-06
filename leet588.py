from typing import List


class FileSystem:
    def __init__(self):
        self.paths = dict()
        self.paths['/'] = 0
        self.files = dict()

    def ls(self, path: str) -> List[str]:
        a = list()
        if path in self.paths:
            for i, j in self.paths.items():
                if j == path.count('/'):
                    a.append(i[1:])
        return a

    def mkdir(self, path: str) -> None:
        if path not in self.paths:
            p = path.split('/')[1:]
            c = 1
            tmp = ""
            for i in p:
                tmp = tmp + '/' + i
                self.paths[tmp] = c
                # print("created: {} @ {}".format(tmp, c))
                c += 1

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath in self.files:
            self.files[filePath] += content
        else:
            self.paths['/' + '/'.join(filePath[1:].split('/')[:-1])] += 1
            self.files[filePath] = content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]


obj = FileSystem()

r = obj.ls("/")
print(r)
obj.mkdir("/a/b/c")
r = obj.ls("/a/b")
print(r)


