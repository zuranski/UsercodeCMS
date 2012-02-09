import os

filelist = [name for name in os.listdir(".") if name.find('output')>-1]
factor = len(filelist)/12+1

file=1
j=0
string = ""
for i in range(len(filelist)):
	string+=filelist[i]+" "
	j+=1
	if j==factor or i==len(filelist)-1:
		print string
		os.system("hadd HTtuple_"+str(file)+".root "+string)
		file+=1
		j=0
		string = ""
