class GridGame:
    def gridGame(self, grid:[[int]])-> int:
        N = len(grid[0])
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()

        for i in range(1,N):
            preRow1[i] += preRow1[i-1]
            preRow2[i] += preRow2[i-1]

        res = float("inf")

        for i in range(N):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i-1] if i>0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
        return res

obj = GridGame()
print(obj.gridGame([[2,5,4],[1,5,1]]))
print(obj.gridGame([[1,3,1,15],[1,3,3,1]]))