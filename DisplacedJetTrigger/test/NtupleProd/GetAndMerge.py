import os,sys

cmssw_dir = os.environ['CMSSW_BASE'] + '/src'
curr_dir = os.getcwd()

#get list of samples
samples = []
for f in os.listdir(cmssw_dir+'/Configuration/GenProduction/test/DisplacedJetProd/cfgFiles/'):
        if f.find("HTo2Long")==-1 : continue
        if f.endswith('pyc') : continue
	name=f[f.find('MH'):f.find('pythia')-1]
	samples.append(name)

# make directory for ntuples
os.mkdir('ntuples')

# get output and merge for each sample

for sample in samples:
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
		
