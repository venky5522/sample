import os

from os.path import join

for (dirnames,dirs,files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.py'):
            thename = os.path.join(dirnames,filename)
            print(os.path.getsize(thename),thename)