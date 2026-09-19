class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


sol = Solution()
assert sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False
assert sol.canAttendMeetings([[7, 10], [2, 4]]) is True
assert sol.canAttendMeetings([]) is True
print("All tests passed")
