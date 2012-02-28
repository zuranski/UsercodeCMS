import os,sys

print "Usage: python GetAndMerge.py datasetfile"

datasetfile = sys.argv[1]
curr_dir = os.getcwd()

# get list of datasets
datasets = open(datasetfile).readlines()
datasets = [line.strip() for line in datasets]
datasets.sort()

# make directory for ntuples
os.mkdir('ntuples')

# get output and merge for each sample

for dataset in datasets:

	sample = dataset[1:dataset.find('7TeV')-1]
	os.chdir('crab/'+sample)
	os.system('crab -status -getoutput')
	crabdir=''
	for name in os.listdir('.'):
		if name.find('crab_0')>-1:
			crabdir = name
	print crabdir
	os.chdir(crabdir+'/res/')
	command1 = 'hadd -f '+sample+'.root *.root'
	command2 = 'mv '+sample+'.root '+curr_dir+'/ntuples'
	print command1
	print command2

	os.system(command1 +' && '+ command2)
	os.chdir(curr_dir)
		
