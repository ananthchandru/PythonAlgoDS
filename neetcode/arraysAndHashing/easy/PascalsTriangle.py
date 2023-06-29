class PascalsTriangle:
    def pascalsTriangle1(self, numRows: int)->[[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])
            res.append(row)  
        return res

    
    #using map    
    def pascalsTriangle2(self, numRows: int)->[[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp1 = res[-1] + [0]
            temp2 = [0] + res[-1]
            res.append([temp1[i]+temp2[i] for i in range(len(temp1))])
        return res[:numRows]
        
        
obj = PascalsTriangle()
print(obj.pascalsTriangle1(5))
print(obj.pascalsTriangle2(5))
