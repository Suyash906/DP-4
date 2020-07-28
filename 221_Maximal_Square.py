# Time Complexity : O(m * n) [m = number of rows n = number of cols]
# Space Complexity : O(m*n) [m = number of rows n = number of cols]
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Problem approach
# 1. Iterate over the matrix and look for '1'
# 2. As soon as we encounter 1, we check the previous row val, col val and diagonal val
# 3. Find the min of the neighbopurs and add 1 to it to square side value for current cell
# 4. Update the max after each 

# Overlapping subproblem - we have to check for the same neighbours value again to determine
# if the current cell forms a bigger square

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        m,n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        max_side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])
                    max_side = max(max_side, dp[i+1][j+1])            
        return max_side * max_side