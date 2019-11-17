import os
count = 0
for (dirnames,dirs,files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.html'):
            count = count+1
print('files',':',count)