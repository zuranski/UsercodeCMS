import os,sys

# directory where crab_fjr files reside
input_dir = sys.argv[1]

for file in os.listdir(input_dir):
	if file.find("crab_fjr")==-1 : continue
	import re
	chop1 = re.compile('<Inputs>.*?</Inputs>',re.DOTALL)
	chop2= re.compile('<InputFile>.*?</InputFile>',re.DOTALL)
	f = open(input_dir+"/"+file)
	data = f.read()
	f.close()
	data = chop1.sub('',data)
	data = chop2.sub('',data)
	f = open ('tmp','w')
	f.write(data)
	f.close()
	os.system('mv tmp '+input_dir+'/'+file)	
