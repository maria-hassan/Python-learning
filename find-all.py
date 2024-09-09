def find(s):
    substring=[]
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            substring.append(s[i:j])
    return substring
s="unifonic is a great company"
res=find(s)
print(res)

