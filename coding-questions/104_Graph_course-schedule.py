# Source: https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Given:
            numCourses: integer, # courses
            prerequisites: a list of edges [a,b] => take b first before a
                1 <= numCourses <= 2000
                0 <= len(prerequisits) <= 5000
                All edges contain nodes that are valid courses (indices in range)
                All edges unique
        Return:
            True if you can finish all courses; false otherwise
        '''
        # Graph: index -> set of indices (course -> prerequisits)
        graph = {i: set() for i in range(numCourses)}
        for [a, b] in prerequisites:
            graph[a].add(b)
        
        color = {i: 'w' for i in range(numCourses)}

        seen = set()
        for i in range(numCourses):
            if i not in seen:
                res = self.visit(graph, i, seen, color)
                if res == False:
                    return False

        return True

    def visit(self, graph, i, seen, color):
        seen.add(i)
        color[i] = 'g'
        for j in graph[i]:
            if j in seen and color[j] == 'g':
                return False
            if j not in seen:
                res = self.visit(graph, j, seen, color)
                if res == False:
                    return False
        color[i] = 'b'
        return True