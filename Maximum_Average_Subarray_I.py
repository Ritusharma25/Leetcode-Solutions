"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> Tuple[float, int]:
        n = len(nums)
        if k > n or k <= 0:
            raise ValueError("Invalid value of k: must be between 1 and length of nums")
        window_sum = sum(nums[:k])
        max_sum = window_sum
        start_index = 0

        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
                start_index = i - k + 1

        max_avg = max_sum / k
        return max_avg
