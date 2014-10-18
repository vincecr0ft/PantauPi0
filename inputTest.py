from ROOT import TFile,TChain,gROOT

import sys

gROOT.ProcessLine(".L loader.C+")

files=sys.argv[-1].split(',')
for filename in files:
   print "adding %s to inputs" % filename
