import os,sys

curr_dir = os.getcwd()

datasets = open('datasets.txt').readlines()
for rawset in datasets:
	rawset = rawset[:-1]
	reconame = rawset[1:rawset.find('TeV')+3]
	print rawset, reconame

	os.chdir('crab/crabjobs/'+reconame)
        os.system('crab -status -getoutput -publish')
        os.chdir(curr_dir)

