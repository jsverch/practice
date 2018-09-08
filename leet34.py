class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        else:
            start = nums.index(target)
            t = 0
            for n in nums[start:]:
                if n == target:
                    t += 1
                else:
                    break
        return [start, start+t-1]


nums = [5, 7, 7, 8, 8, 9, 10, 10, 11, 13, 13, 42]
target = 8

if __name__ == '__main__':
    print Solution().searchRange(nums, target)
