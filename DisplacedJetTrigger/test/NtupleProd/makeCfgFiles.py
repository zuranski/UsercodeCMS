import os,sys

print "Usage: python makeCfgFiles.py Trig_Version isOpen"

version = sys.argv[1]
isOpen = int(sys.argv[2])

cmssw_dir = os.environ['CMSSW_BASE'] + '/src'
curr_dir = os.getcwd()

#get list of samples
samples = []
for f in os.listdir(cmssw_dir+'/MyAnalysis/DisplacedJetTrigger/python/'):
        if f.find("MH_")==-1 : continue
        if f.endswith('pyc') : continue
	name=f[f.find('MH'):f.find('cff')-1]
	samples.append(name)

# get list of datasets
datasets = open('datasets.txt').readlines()
datasets = [line.strip() for line in datasets]

samples.sort()
datasets.sort()

# prepare CMS cfg filenames
cfgfilename = 'runMC.py' 
trigfilename = 'myhlt_'+('open_' if isOpen else '')+'mcV'+version+'.py'
if not os.path.isfile('../../python/'+trigfilename):
	print 'No Trigger File'
	sys.exit()

# prepare main cfg file
cfgfile = open('../'+cfgfilename).read()
import re
cfgfile=re.sub('myhlt_.*import',trigfilename[:-3]+' import',cfgfile,re.DOTALL)

# loop over samples and submit to crab
for sample,dataset in zip(samples,datasets):

	os.mkdir('crab/'+sample)
	template = open('crab.cfg')
	tmpcfg = open('tmpcfg','write')
	for line in template:
		if line.find('datasetpath') > -1:
			line = 'datasetpath='+dataset+'\n'	
		if line.find('pset')>-1:
			line = 'pset='+cfgfilename+'\n'
		if line.find('output_file')>-1:
			line = 'output_file='+sample+'.root'+'\n'
		tmpcfg.write(line)
	tmpcfg.close()
	os.system('mv tmpcfg crab/'+sample+'/crab.cfg')
	cfgfile=re.sub('fileName.*root','fileName = cms.string(\''+sample+'.root',cfgfile,re.DOTALL)
	f = open('crab/'+sample+'/'+cfgfilename,'w')
	f.write(cfgfile)
	f.close()

	# create and submit crab jobs
	os.chdir('crab/'+sample)
	#os.system('crab -create -submit')
	os.chdir(curr_dir)
