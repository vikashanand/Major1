
import glob

important = []
path = '/home/vikash/PycharmProjects/Major1/TestData/Firewall/*.txt'
files=glob.glob(path)

for file in files:
    f=open(file, 'r')
    r=f.readlines()
    for line in r:
        important.append(line)
    f.close()
print(important)



