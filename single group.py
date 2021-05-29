import re
mystr = "this is my string"
substr = "this"
print(re.match(substr , mystr))
print(re.match("is",mystr))
print(re.search("is", mystr))
mystr2 = "this is code program of python laguage 123"
substr = "code"
print(re.search(substr, mystr2))
matchobj = re.search("of", mystr2)
if matchobj:
    print("obj foumd")
else:
    print("not found")
print(re.search("123", mystr2))
print(re.search("python", mystr2))
print(re.match("this", mystr2))







import re
def search_string(substr, mystr):
    matchobj = re.search(substr, mystr)
    if matchobj:
        return "it is found"
    else:
        return "it is not found"
mystr = "this is fourth month and python program itself offline "
substr = "this"
s = "this is \t my string"
print(s)

