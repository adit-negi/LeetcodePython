class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = defaultdict(list)
        for i in range(len(arr)):
            if i+arr[i]< len(arr):
                graph[i].append(i+arr[i])
            if i-arr[i]>=0:
                graph[i].append(i-arr[i])
        def isReachable( s, d,graph): 
            visited =[False]*(len(arr)) 
            queue=[] 
            queue.append(s) 
            visited[s] = True

            while queue: 
                n = queue.pop(0) 
                if arr[n] == d: 
                    return True
                for i in graph[n]: 
                    if visited[i] == False: 
                        queue.append(i) 
                        visited[i] = True
            return False
        return isReachable(start,0,graph)
