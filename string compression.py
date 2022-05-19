class Solution:
    def compress(self, chars: List[str]) -> int:
        s = chars[0]
        cnt = 1
        j = 1
        for i in chars[1:]:
            if i == s[-1]:
                cnt += 1
            else:
                if cnt != 1:
                    s += str(cnt)
                    for k in str(cnt):
                        chars[j] = k
                        j += 1
                    cnt = 1
                s += i
                chars[j] = i
                j += 1
        if cnt != 1:
            s += str(cnt)
            for k in str(cnt):
                chars[j] = k
                j += 1        
        
        chars[:] = chars[:len(s)]
        return len(chars)
