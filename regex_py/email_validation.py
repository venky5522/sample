import re
user_input=input("enter your input")
mat=re.match(r"(^[a-zA-Z]+[.a-zA-Z0-9_+-]+@[a-zA-Z]+\.[a-z]+$)",user_input)
#mat=re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$)",user_input)
#mat = re.match(r"\b[A-Z0-9.%+-]+@+[A-Z0-9.-]+\.[A-Z]{2,}",user_input,re.I)
if mat:
    print(user_input,"is valid gmail")
else:
    print(user_input,"is invalid gmail")
