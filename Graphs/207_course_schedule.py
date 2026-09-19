class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=done

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
            return True

        return all(dfs(course) for course in range(numCourses))


sol = Solution()
assert sol.canFinish(2, [[1, 0]]) is True
assert sol.canFinish(2, [[1, 0], [0, 1]]) is False
assert sol.canFinish(1, []) is True
print("All tests passed")
