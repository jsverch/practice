from typing import List


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], eid: int) -> int:
        # convert list to hash map
        emps = {emp.eid: emp for emp in employees}
        total = 0
        dfs(eid)
        return total

    def dfs(self, eid):
        total = total + emps[eid].importance
        list(map(self.dfs, self.emps[eid].subordinates))
        return


obj = Solution()

print(obj.getImportance([[1,5,[2,3]],[2,3,[]],[3,3,[]]], 1))