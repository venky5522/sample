my_str = "my new life"
for i in my_str.split():
    emp_str = " "
    for j in range(len(i)):
        emp_str = emp_str+i[len(i)-j-1]
    print(''.join(emp_str),end=" ")




