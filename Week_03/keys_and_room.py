class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        dic = dict()
        l = len(rooms)
        for i, room in enumerate(rooms):
            dic[i] = room
        visited = set()

        def DFS(i):
            if i in visited: return

            visited.add(i)
            for room in dic[i]:
                DFS(room)

        DFS(0)
        return True if len(visited) == l else False
