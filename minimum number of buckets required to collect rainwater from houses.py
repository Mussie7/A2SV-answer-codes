class Solution:
    def minimumBuckets(self, street: str) -> int:
        if street == "H":
            return -1
        if street[0] == "H" and street[1] != ".":
            return -1
        if street[-1] == "H" and street[-2] != ".":
            return -1
        
        output = r = 0
        while r < len(street):
            if street[r] == "H" and r + 1 < len(street):
                if street[r+1] == "." and r + 2 < len(street):
                    if street[r+2] == "H":
                        output += 1
                        r += 3
                    else:
                        output += 1
                        r += 1
                elif street[r+1] != "." and street[r-1] == ".":
                    r += 1
                    output += 1
                elif street[r+1] != "." and street[r-1] != ".":
                    return -1
                else:
                    output += 1
                    r += 1
            elif street[r] == ".":
                r += 1
            else:
                output += 1
                r += 1
        
        return output
