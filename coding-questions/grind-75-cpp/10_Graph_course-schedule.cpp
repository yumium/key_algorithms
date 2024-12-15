class Solution {
public:
    /*
        Given:
            numCourses: # of courses
                1 <= numCourses <= 2000
            prerequisites: [[a,b]] meaning b before a
                0 <= prerequisites.size() <= 5000
                all pairs, values are valid courses
                all pairs unique
        
        Return:
            Whether you can finish the courses

        Obs:
        - Courses are nodes
        - Direct edge A -> B if A is a prereq for B
        - Topological sort possible iff graph is acyclic
        - canFinish iff no cycles in graph
        - DFS, cycls iff there are back edges

        TIME: O(V+E) = O(numCourses + prerequisites)
        SPACE: O(numCourses)
    */
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<set<int>> graph = makeGraph(numCourses, prerequisites);
    
        set<int> seen;
        set<int> grey;
        for (int course = 0; course < numCourses; course++) {
            if (seen.find(course) == seen.end()) {
                if (!visit(course, graph, seen, grey))
                    return false;
            }
        }
        
        return true;
    };

    bool visit(int course, vector<set<int>>& graph, set<int>& seen, set<int>& grey) {
        grey.insert(course);
        seen.insert(course);
        for (auto nextCourse : graph[course]) {
            if (grey.find(nextCourse) != grey.end() || (seen.find(nextCourse) == seen.end() && !visit(nextCourse, graph, seen, grey)))
                return false;
        }
        grey.erase(course);
        return true;
    }

    vector<set<int>> makeGraph(int numCourses, vector<vector<int>>& prerequisites) {
        vector<set<int>> res {static_cast<size_t>(numCourses)};
        for (auto pair : prerequisites) {
            res[pair[1]].insert(pair[0]);
        }

        return res;
    }
};