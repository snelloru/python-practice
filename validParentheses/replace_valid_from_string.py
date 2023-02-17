def isValid(s):
        s = s.replace('()','')
        s = s.replace("{}",'')
        s = s.replace("[]",'')
        return len(s) == 0

print(isValid("{}"))
print(isValid("()[]{}"))
print(isValid("{}{)[]"))
