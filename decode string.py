class Solution:
    def decodeString(self, s: str) -> str:
        k_stack = []
        str_stack = []
        st = list(s)
        
        return self.decoder(k_stack,str_stack,st)
        
    
    def decoder(self, k_stack,str_stack, st):
        message = ""
        if not st:
            return "".join(str_stack)
        if st[0].isnumeric():
            k_stack.append(st.pop(0))
            while st[0].isnumeric():
                k_stack[-1] += st.pop(0)
        elif st[0] == "]":
            while str_stack and str_stack[-1] != "[":
                message = str_stack.pop() + message
            st.pop(0)
            str_stack.pop()
            message *= int(k_stack.pop())
            str_stack.append(message)
        else:
            str_stack.append(st.pop(0))
            
        return self.decoder(k_stack,str_stack,st)
