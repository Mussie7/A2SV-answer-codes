class Solution:
    def numberToWords(self, num: int) -> str:
        suffix = ["", "Thousand", "Million", "Billion", "Trillion"]
        word = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        num = list(str(num))
        count = 0
        return self.speller(num,word,suffix,count)
        
    def speller(self, num: list, word: list, suffix: list, count: int) -> str:
        output = ""
        if len(num) > 2:
            temp = num[-3:]
            for i in range(len(temp)):
                if i != 1:
                    if temp[i] == "0":
                        continue
                    output += word[int(temp[i])] + " "
                    if i == 0:
                        output += "Hundred "
                elif i == 1:
                    if temp[i] == "1":
                        output += word[int(str(i)+temp[i+1])] + " "
                        break
                    elif 1 < int(temp[i]) < 10:
                        output += word[20 + int(temp[i]) - 2] + " "
            if count != 0 and output != "":
                output += suffix[count] + " "
            count += 1
            if len(num) == 3:
                return output[:-1]
            if output == "":
                return self.speller(num[:-3],word,suffix,count)
            return self.speller(num[:-3],word,suffix,count) + " " + output[:-1]
        elif len(num) == 2:
            for i in range(len(num)):
                if i == 0:
                    if num[i] == "1":
                        output += word[int("1"+num[i+1])] + " "
                        break
                    elif 1 < int(num[i]) < 10:
                        output += word[20 + int(num[i]) - 2] + " "
                else:
                    if num[i] != "0":
                        output += word[int(num[i])] + " "
            if count == 0:
                return output[:-1]
            output += suffix[count]
            return output
        elif len(num) == 1:
            if count == 0 and num[0] == "0":
                return "Zero"
            output += word[int(num[0])]
            if count == 0:
                return output
            return output + " " + suffix[count]
