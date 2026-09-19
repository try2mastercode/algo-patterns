class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


sol = Solution()
assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
assert sol.carFleet(10, [3], [3]) == 1
assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
print("All tests passed")
