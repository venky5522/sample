'''text = """python
selenium
java
django"""
import re
a = re.split(r'\n',text)
print(a)'''
import re
'''print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))'''
'''print(re.split('[a-f]+', 'Aey, Boy oh boy, come here',flags=re.IGNORECASE))'''
print(re.split('[a-f]+','Aey, Boy oh boy, come here'))



