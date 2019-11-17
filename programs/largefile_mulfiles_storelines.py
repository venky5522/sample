lines_per_page = 200
smallfile = None
Get_path = r"C:\Users\pravallika p\PycharmProjects\classprograms\trail.py"
with open(Get_path) as my_file:
    for lineno, line in enumerate(my_file):
        if lineno % lines_per_page==0:
            if smallfile:
                smallfile.close()
            small_filename = 'new_file_{}.txt'.format(lineno+lines_per_page)
            smallfile = open(small_filename,'w')
        smallfile.write(line)
    if smallfile:
        smallfile.close()
