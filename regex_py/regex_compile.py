import re
p = re.compile("\d")
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
q = re.compile("\d+")
print(q.findall("I went to him at 11 A.M. on 4th July 1886"))
r = re.compile("ab*")
print(r.findall("ababbbaaabbab"))

