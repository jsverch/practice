from typing import List
import heapq

# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         tr = 0
#         while intervals:
#             ce = -1
#             print(sorted(intervals))
#             s_l = list()
#             for i in sorted(intervals):
#                 start, end = i
#                 if start < ce:
#                     print('We need another room for : {}'.format(i))
#                     s_l.append(i)
#                 else:
#                     ce = end
#             tr += 1
#             intervals = s_l
#         return tr


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_rooms = []
        intervals.sort(key=lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])
        print(free_rooms)

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
            print(free_rooms)
        return len(free_rooms)



obj = Solution()

r = obj.minMeetingRooms([[9, 10], [4, 9], [9, 17], [0, 60], [17,45]])

print("{} rooms needed".format(r))