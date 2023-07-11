class BrickWall:
    def leastBricks(self, wall: [[int]]) -> int:
        res = {0: 0}
        for brick in wall:
            sum = 0
            for i in range(len(brick) - 1):
                sum += brick[i]
                res[sum] = 1 + res.get(sum, 0)

        return len(wall) - max(res.values())

obj = BrickWall()
print(obj.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
print(obj.leastBricks([[1],[1],[1]]))
print(obj.leastBricks([]))