class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        i = 0
        n = len(chars)

        while i < n:                          
            ch = chars[i]
            count = 0

            while i < n and chars[i] == ch: 
                count += 1
                i += 1

            chars[idx] = ch                 
            idx += 1

            if count > 1:                    
                for dig in str(count):
                    chars[idx] = dig
                    idx += 1

        return idx