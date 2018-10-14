class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        combined = list()
        while True:
            try:
                nums1[0]
            except:
                combined += nums2
                break
            try:
                nums2[0]
            except:
                combined += nums1
                break
            if nums1[0] <= nums2[0]:
                combined.append(nums1[0])
                del nums1[0]
            elif nums2[0] < nums1[0]:
                combined.append(nums2[0])
                del nums2[0]
        if len(combined) % 2:
            return float(combined[len(combined) / 2])
        else:
            i = len(combined) / 2
            return (combined[i-1] + combined[i]) / 2.0
        # print combined


print Solution().findMedianSortedArrays([1], [1])

