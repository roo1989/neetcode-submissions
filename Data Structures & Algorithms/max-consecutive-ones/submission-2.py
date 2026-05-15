class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        1,1,0,1,1,1
        ^ current = 1, longest = current
          ^ current = 2, longest = current
            ^ current = 0
                ^ current = 1, if longest < current, longest = current
        """

        current = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                if longest < current:
                    longest = current
            else:
                current = 0

        return longest