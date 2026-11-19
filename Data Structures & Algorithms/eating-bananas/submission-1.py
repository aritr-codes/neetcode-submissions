class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            total_hrs = 0
            for pile in piles:
                total_hrs += (pile + k - 1) // k
            return total_hrs <= h

        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1
        return l