class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        noname = {
            'V': 'I',
            'X': 'I',
            'L': 'X',
            'C': 'X',
            'M': 'C',
            'D': 'C',
            'I': '-'
        }
        res = 0
        prev_sym = ''
        for symbol in reversed(s):
            if prev_sym and noname[prev_sym] == symbol:
                res -= val[symbol]
            else:
                res += val[symbol]
                prev_sym = symbol
        return res
