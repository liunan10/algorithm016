#bfs
#shortest operations to target
#forward A: speed*2, position += speed
#R: speed = -1 if speed > 0 else 1, position no change
class Solution:
    def racecar(self, target: int) -> int:
        if target == 0: return 0
        if target == 1: return 1
        visited = set()
        visited.add((0, 1)) #position, speed
        from collections import deque
        queue = deque([(0, 1)])
        res = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                position, speed = queue.popleft()
                if position == target:
                    return res
                for neighbor in self.get_neighbors(position, speed, target):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            res += 1
        return res

    def get_neighbors(self, position, speed, target):
        neighbors = []
        new_position = position + speed
        if new_position > 0 and new_position <= target << 1:
            neighbors.append((new_position, speed << 1))
        if speed > 0:
            neighbors.append((position, -1))
        else:
            neighbors.append((position, 1))
        return neighbors

            
#dp
#dp[i]: minimum operations to reach i
#two scenarios:
# > i, then back
#forward = 1<< cnt_forward , 
# <i, back, back, to i

class Solution:
    def racecar(self, target: int) -> int:
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for i in range(1, target + 1):
            k = i.bit_length()
            if i == (1 << k) - 1:
                dp[i] = k
                continue
            dp[i] = min(dp[i], k + 1 + dp[(1 << k) - 1 - i]) #7
            for m in range(k - 1):
                dp[i] = min(dp[i], k + 1 + m + dp[i - (1 << (k - 1)) + (1 << m)])
        return dp[target]

             
