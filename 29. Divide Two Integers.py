class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == 0:
            return 0
        if divisor == 0:
            raise ValueError("Divisor cannot be zero.")

        
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        
        negative = (dividend < 0) != (divisor < 0)

        
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            dividend -= temp_divisor
            quotient += multiple

        if negative:
            quotient = -quotient

        return min(max(quotient, INT_MIN), INT_MAX)
