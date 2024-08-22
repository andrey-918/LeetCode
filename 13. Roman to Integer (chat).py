class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_map[char]

            # If the current value is less than the previous value, we subtract
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Update previous value
            prev_value = current_value

        return total
