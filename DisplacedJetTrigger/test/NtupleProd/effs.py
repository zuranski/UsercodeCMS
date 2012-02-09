import ROOT as r
import os

for file in os.listdir('ntuples/'):

	rfile = r.TFile('ntuples/'+file)
	tree = rfile.Get('trigtuple').Get('tree')
	N = tree.GetEntries()

	single = 0
	double = 0

	for i in range(N):
		tree.GetEntry(i)
		for trig in tree.triggers:
			if trig.find('Single')>-1: single+=1
			if trig.find('Double')>-1: double+=1

	print file[:-5], str(round(100*single/float(N),1)), str(round(100*double/float(N),1))
	
