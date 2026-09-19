import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)


sol = Solution()
assert sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
assert sol.minMeetingRooms([[7, 10], [2, 4]]) == 1
assert sol.minMeetingRooms([]) == 0
print("All tests passed")
