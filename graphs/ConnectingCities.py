class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
                
        edges=len(connections)  
        
        if edges < N-1:    #Edge case if edges are less than the vertices
            return -1
        
        heaplist=[]  
        parents={}
        
        def getParent(node):    #Helper function to get the parents
            parent=parents[node]
            while node!=parent:
                node=parent
                parent=parents[parent]
            return node     

        for node in range(N+1):   #Initialize the parent map, initially the node's parent is itself
            parents[node]=node
        
        for vert1, vert2 , cost in connections: #Maintain a min heap (You can sort the list as well) to have the minimum edge node always on top of the heap
            heapq.heappush(heaplist,[cost,vert1,vert2])

        min_cost=0
        edge_count=0
        
        while heaplist:
            #Pop the min edge 
            cost, parent, child = heapq.heappop(heaplist)
            
            #Get the parents of the vertices of parent and child
            p1=getParent(parent)
            p2=getParent(child)
            
            #Check if the parents are not same
            if p1 != p2:
                parents[p2] = p1  #Update the parent of the child
                min_cost+=cost
                edge_count+=1
                
                #End Case: If the edge count is N-1
                if edge_count == N-1:
                    return min_cost

        return -1           
            
