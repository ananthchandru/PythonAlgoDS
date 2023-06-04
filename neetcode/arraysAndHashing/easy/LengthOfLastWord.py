class LengthOfLastWord:
    def length(self, str: str)->int:
        listOfWords = str.split()
        return len(listOfWords[-1])
        
        
obj = LengthOfLastWord()
print(obj.length("Hello World"))
print(obj.length("    fly me   to   the moon  "))
