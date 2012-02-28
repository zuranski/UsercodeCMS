import os,sys

print "Usage: python makeCfgFiles.py datasetfile pycfgfile crabtemplate"

datasetfile = sys.argv[1]
pycfgfile = sys.argv[2]
crabfile = sys.argv[3]

curr_dir = os.getcwd()

# get list of datasets
datasets = open(datasetfile).readlines()
datasets = [line.strip() for line in datasets]
datasets.sort()

# prepare main cfg file
cfgfile = open('../'+pycfgfile).read()

# loop over samples and submit to crab
for dataset in datasets:

	sample = dataset[1:dataset.find('7TeV')-1]
	os.mkdir('crab/'+sample)
	template = open(crabfile)
	tmpcfg = open('tmpcfg','write')
	for line in template:
		if line.find('datasetpath') > -1:
			line = 'datasetpath='+dataset+'\n'	
		if line.find('pset')>-1:
			line = 'pset='+pycfgfile+'\n'
		if line.find('output_file')>-1:
			line = 'output_file='+sample+'.root'+'\n'
		tmpcfg.write(line)
	tmpcfg.close()
	os.system('mv tmpcfg crab/'+sample+'/crab.cfg')
	import re
	cfgfile=re.sub('fileName.*root','fileName = cms.string(\''+sample+'.root',cfgfile,re.DOTALL)
	f = open('crab/'+sample+'/'+pycfgfile,'w')
	f.write(cfgfile)
	f.close()

	# create and submit crab jobs
	os.chdir('crab/'+sample)
	os.system('crab -create -submit')
	os.chdir(curr_dir)
