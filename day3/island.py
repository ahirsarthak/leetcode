# LC - 200 . No of ISLANDS


def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, col = len(grid), len(grid[0])
    islands = 0
    visit = set()

    def dfs(r, c):
        if (r not in range(rows) or c not in range(col) or (r, c) in visit or grid[r][c] == "0"):
            return
        visit.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            dfs(r+dr, c+dc)

    for r in range(rows):
        for c in range(col):
            if grid[r][c] == "1" and (r, c) not in visit:

                islands += 1
                dfs(r, c)
    return islands
