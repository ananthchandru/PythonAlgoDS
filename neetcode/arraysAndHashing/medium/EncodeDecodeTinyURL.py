class Codec:

    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        shortUrl = self.base + str(len(self.encodeMap) + 1)
        self.encodeMap[longUrl] = shortUrl
        self.decodeMap[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]

# class Codec:

#     def __init__(self):
#         self.urls = []

#     def encode(self, longUrl):
#         self.urls.append(longUrl)
#         return 'http://tinyurl.com/' + str(len(self.urls) - 1)

#     def decode(self, shortUrl):
#         return self.urls[int(shortUrl.split('/')[-1])]


# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
encodedUrl = codec.encode(url)
print(encodedUrl)
print(codec.decode(encodedUrl))