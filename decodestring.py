class Solution:
    def decodeString(self, s: str) -> str:
        numberStack = []
        stringStack = []
    
        for char in s:
            if char.isdigit():
                numberStack.append(int(char))
            elif char == '[':
                stringStack.append('[')
            elif char != ']':
                stringStack.append(char)
            else:
                temp = ""
                while stringStack[-1] != '[':
                    temp = stringStack.pop() + temp
                stringStack.pop()        # pop '['
                num = numberStack.pop()  # pop number
                repeated = temp * num
                for c in repeated:
                    stringStack.append(c)
    
        return "".join(stringStack)
