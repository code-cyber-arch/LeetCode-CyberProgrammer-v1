class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  
        max_length = 0 
        start = 0  

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            char_index[s[end]] = end 
            current_length = end - start + 1  
            max_length = max(max_length, current_length)  

        return max_length
