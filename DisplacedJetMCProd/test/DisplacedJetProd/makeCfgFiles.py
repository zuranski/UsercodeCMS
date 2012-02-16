import os

os.mkdir('cfgFiles')
for f in os.listdir('../../python'):
	if f.find("HTo2Long")==-1 : continue
	if f.endswith('pyc') : continue
	command = "cmsDriver.py MyAnalysis/DisplacedJetMCProd/python/"+f+" \
 --step GEN:ProductionFilterSequence,SIM,DIGI,L1,DIGI2RAW,HLT:GRun\
 --beamspot Realistic7TeVCollision\
 --fileout GEN-SIM-RAWDEBUG.root\
 --conditions START50_V10::All\
 --pileup E7TeV_Ave23_50ns\
 --datamix NODATAMIXER\
 --eventcontent RAWDEBUG\
 --datatier GEN-SIM-RAWDEBUG\
 -n 500\
 --no_exec  "
	os.system(command)
	os.system('mv HTo2* cfgFiles/')

os.mkdir('crab/crabjobs')
for f in os.listdir('cfgFiles/'):

	if f.endswith('pyc') : continue
	file = open('cfgFiles/'+f,)
	tmp = open('tmp','write')
	for line in file:
		if line.strip == "" : continue
		if line.find('input = cms.untracked.int32(500)')>-1:
			line = line.replace('input','output')
		if line.find("6, 11, 13, 15),")>-1:
			line = line.replace(', 11, 13, 15','')
		if line.find("6000111, 6000112, 6000113")>-1:
			line = line.replace(', 6000113','')

		tmp.write(line)

	os.system('mv tmp cfgFiles/'+f)
	name=f[f.find('MH'):f.find('pythia')-1]
	os.mkdir('crab/crabjobs/'+name)
	template = open('crab.cfg')
	tmp = open('tmp','write')
	for line in template:
		if line.find('pset=') > -1:
			line='pset=../../cfgFiles/'+f+"\n"
		if line.find('publish_data_name=') > -1:
			line='publish_data_name='+name+'GEN_SIM_RAWDEBUG\n'
		tmp.write(line)
	os.system('mv tmp crab/crabjobs/'+name+'/crab.cfg')

