class EncodeDecode:
    def encode(self, strList: [str]) -> str:
        res = ""
        for s in strList:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, encodedStr: str) -> [str]:
        res = []
        i = 0
        while i<len(encodedStr):
            j = i
            while encodedStr[j] !="#":
                j+=1
            length = int(encodedStr[i:j])
            res.append(encodedStr[j+1:j+1+length])
            i = j+1+length
        return res

    def decode1(self, encodedStr: str) -> [str]:
        res = []
        i = 0
        while i<len(encodedStr):
            if(encodedStr[i+1]=="#"):
                length = int(encodedStr[i])
                res.append(encodedStr[i+2:i+2+length])
                i = i+2+length
        return res

obj = EncodeDecode()
encodedStr = obj.encode(["I","Have","3", "3#", "cars"])
print(encodedStr)
print(obj.decode1(encodedStr))
