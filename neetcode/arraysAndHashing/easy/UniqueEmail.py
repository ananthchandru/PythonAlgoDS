class UniqueEmail:
    def uniqueEmail1(self, strs:[str])->int:
        uniqueEmails = set()
        for email in strs:
            local,domain = email.split("@")
            local = local.split("+")[0].replace(".","")
            uniqueEmails.add(local+"@"+domain)
#        print(uniqueEmails)
        return len(uniqueEmails)
        
    #without using split, replace    
    def uniqueEmail2(self, strs:[str])->int:
        uniqueEmails = set()
        for str in strs:
            i = 0
            local = ""
            while(str[i] != "@"):
                if str[i] == "+":
                    break
                if(str[i]!="."):
                    local += str[i]
                i+=1
                
            if(str[i]=="+"):
                while(str[i]!="@"):
                    i+=1
            local += "@" + str[i+1:]
            print(local)
            uniqueEmails.add(local)
        return len(uniqueEmails)
        
        
        
obj = UniqueEmail()
print(obj.uniqueEmail1(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(obj.uniqueEmail1(["a@leetcode.com","b@leetcode.com","c+d@leetcode.com"]))

print(obj.uniqueEmail2(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(obj.uniqueEmail2(["a@leetcode.com","b@leetcode.com","c+d@leetcode.com"]))
