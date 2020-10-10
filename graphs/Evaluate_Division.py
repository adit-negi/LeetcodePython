class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        
        def backtrack_evalutate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret =-1.0
            nei = graph[curr_node]
            if target_node in nei:
                ret = acc_product* nei[target_node]
                
            else:
                for neighbor, value in nei.items():
                    if neighbor in visited:
                        continue
                    ret  = backtrack_evalutate(neighbor,target_node,acc_product*value,visited)
                    
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret
        
        for (div, dis), value in zip(equations, values):
            graph[div][dis]=value
            graph[dis][div]=1/value
            
        results = []
        
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0
                
            elif dividend == divisor:
                ret = 1.0
            
            else:
                visited = set()
                ret = backtrack_evalutate(dividend, divisor,1 , visited)
                
            results.append(ret)
            
        return results
