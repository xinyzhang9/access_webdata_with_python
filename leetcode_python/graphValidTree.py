# dfs
def validTree(self, n, edges):
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return len(edges) == n-1 and not neighbors

#union find
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def find(i):
            while root[i] != i:
                i = root[i]
            return i
        def union(x,y):
            i,j = find(x),find(y)
            root[i] = j
        if n-1 != len(edges):
            return False
        root = [i for i in range(n)]
        for e in edges:
            if find(e[0]) == find(e[1]):
                return False
            union(e[0],e[1])
        
        return True
