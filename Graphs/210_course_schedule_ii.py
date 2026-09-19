class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=done
        order = []

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            state[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return order


sol = Solution()
assert sol.findOrder(2, [[1, 0]]) == [0, 1]
assert sol.findOrder(1, []) == [0]
assert sol.findOrder(2, [[1, 0], [0, 1]]) == []
print("All tests passed")
