class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for word in strs:
            index = 0
            while index < len(word) and index < len(answer):
                if word[index] == answer[index]:
                    index += 1
                else:
                    answer = ''
            answer = word[:index]
        return answer
