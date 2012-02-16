import os

curr_dir = os.getcwd()
os.mkdir('crab/crabjobs')
datasets = open('datasets.txt').readlines()
for rawset in datasets:
	rawset = rawset[:-1]
	reconame = rawset[1:rawset.find('TeV')+3]
	print rawset, reconame

	os.mkdir('crab/crabjobs/'+reconame)
	template = open('crabReco.cfg')
	tmpcfg = open('tmpcfg','write')
	for line in template:
		if line.find('datasetpath=') > -1:
			line='datasetpath='+rawset+"\n"
		if line.find('publish_data_name=') > -1:
			line='publish_data_name='+reconame+'_GEN_SIM_RECODEBUG\n'
		tmpcfg.write(line)
	tmpcfg.close()
	os.system('mv tmpcfg crab/crabjobs/'+reconame+'/crab.cfg')
	os.system('cp reco_RAW2DIGI_RECO.py crab/crabjobs/'+reconame+'/')
	os.chdir('crab/crabjobs/'+reconame)
	os.system('crab -create -submit')
	os.chdir(curr_dir)
