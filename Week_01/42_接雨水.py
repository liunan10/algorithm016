class Solution:
    # 单调栈
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack: break
                left, right = stack[-1], i
                ans += (right - left - 1) * (min(height[right], height[left]) - height[top])
            stack.append(i)
        return ans

class Solution:
    # 双指针夹逼
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]: #左边开始积水
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:                            #右边开始积水
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
                
        
	
