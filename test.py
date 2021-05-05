import os

path ="D:\School\Year 4\LP4\Statistical learning for big data"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))
		
for name in filelist:
	print(name)
	
filelist_new = []
for name in filelist:
	name_new = name.split('\\')
	for i,name in enumerate(name_new):
		if name == 'LP4':
			name_new[i] = 'LP4a'
	filelist_new.append('\\'.join(name_new))

for name in filelist_new:
	print(name)
	