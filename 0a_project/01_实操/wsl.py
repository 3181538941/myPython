import os
a = os.popen("ls -m").readline()
print(a)
print(type(a))
