#https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #bfs
        edges = collections.defaultdict(list)
        indegree = [0]*numCourses
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indegree[info[0]] += 1
            
        q = collections.deque([u for u in range(numCourses) if indegree[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return visited == numCourses
        
        '''
        #dfs
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)
        
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        return valid
        '''
