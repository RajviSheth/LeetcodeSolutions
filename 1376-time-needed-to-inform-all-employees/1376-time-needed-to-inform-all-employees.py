class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = collections.defaultdict(list)
        for idx in range(n):
            adj[manager[idx]].append(idx)
            
        q = deque([(headID, 0)])
        res = 0
        while q:
            id_, time = q.popleft()
            res = max(res, time)
            for emp in adj[id_]:
                q.append((emp, time + informTime[id_]))
        return res
                
        