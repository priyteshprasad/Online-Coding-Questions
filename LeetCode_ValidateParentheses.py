# LeetCode question: Valid Paranthesis
# verify if the order of Paranthesis is correct or not


def isValid(s: str) -> bool:
        n = len(s)
        stack = []
        myDict = {'(': ')', '[':']', '{': '}'}
        for i in s:
            if stack and stack[-1] in "([{" and myDict[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
        return not stack


print(isValid("{}[()]")) #True
print(isValid("{}[(){")) #False