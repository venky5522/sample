file_names = ['file1.txt','file2.txt']
with open('venky_file.txt','w') as venky_file:
    for file in file_names:
        with open(file) as new_file:
            venky_file.write(new_file.read())
print("file opened successfully and add the data successfully!!!!")