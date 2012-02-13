import ROOT as r
import os

print "sample doubleDJ singleDJ doubleDJbackup SingleDJbackup"
for file in os.listdir('ntuples/'):

	rfile = r.TFile('ntuples/'+file)
	tree = rfile.Get('trigtuple').Get('tree')
	N = tree.GetEntries()
	#N = 1000

	names = ['HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_v1','HLT_HT250_L1FastJet_SingleDisplacedPFJet60_v1','HLT_HT250_L1FastJet_DoubleDisplacedPFJet60_ChgFraction10_v1','HLT_HT250_L1FastJet_SingleDisplacedPFJet60_ChgFraction10_v1']

	effs = [0]*4

	for i in range(N):
		tree.GetEntry(i)
		for trig in tree.triggers:
			for i in range(4):
				if trig==names[i]: effs[i]+=1

	effs = [str(round(100*a/float(N),3)) for a in effs]
	print file[:-5], " ".join(a for a in effs)
