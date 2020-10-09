class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False]*len(rooms)
        seen[0]= True
        stack =[0]
        while stack:
            nodes = stack.pop()
            for node in rooms[nodes]:
                if not seen[node]:
                    seen[node]=True
                    stack.append(node)
        return all(seen)
