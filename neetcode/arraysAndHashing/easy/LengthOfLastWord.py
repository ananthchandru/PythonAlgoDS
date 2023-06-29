class LengthOfLastWord:

    def length(self, s:str)->int:
        lastWord = 0
        for i in range(len(s) - 1, -1, -1):
        #for i in s[::-1]:
            if s[i] == " ":
                if lastWord > 0:
                    return lastWord
            else:
                lastWord += 1
        return lastWord

    def length1(self, str: str)->int:
        listOfWords = str.split()
        return len(listOfWords[-1])
        
        
obj = LengthOfLastWord()
print(obj.length("Hello World"))
print(obj.length("    fly me   to   the moon  "))
print(obj.length1("Hello World"))
print(obj.length1("    fly me   to   the moon  "))
