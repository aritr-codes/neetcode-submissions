class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        def get_next(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            return total
        
        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if slow == 1 or fast == 1:
                return True
            
            if slow == fast:
                return False