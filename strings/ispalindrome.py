s = "A man, a plan, a canal: Panama"

s = s.replace(" ", "")
a = ""
for i in range(len(s)):
    if s[i].isalnum():
        a = a+s[i]
a = a.lower()
print(a)
