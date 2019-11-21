import urllib
data = urllib.request.urlopen('https://iopscience.iop.org/0004-637X/805/1/3/suppdata/apj511597t8_mrt.txt')
for line in data : print(line)
data.close()
