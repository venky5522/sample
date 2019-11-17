'''import time
print(time.gmtime(0))
print(time.localtime(time.time()))
print(time.time())'''
import time
time_here = time.localtime()
print(time_here)
print("Year: ",time_here[0])
print("Month: ",time_here[1])
print("Day: ",time_here[2])
