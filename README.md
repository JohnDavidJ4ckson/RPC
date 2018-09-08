# RPC
Hit rates distribution of RPC
This repository was built in order to produce plots relevant for background studies of the RPC subdetector of CMS.

The comparison plots between DT and RPC hit rates vs phi can be produced by running the script DT/phiRatioRPCvsDT.py
The script was tested in a computer with Root version 6.12/04 as printed by the command gROOT->GetVersion() 
Note that this comparison being modified in order to comply with the granularity of interest, hence this version of
the code will not even produce the plots integrated over all wheels. This is because the script imports DT/phiDistroRPC
and DT/generateDTTGraphs both of which are being revisited.


The comparison plots that include CSC, DT and RPC hit rates vs pseudorapidity are produced by the script CSC/etaDistro.py
The script imports CSC/generateDTTGraphs and CSC/generateCSCTGraphs in order to add the information from these detectors to
the previous plots which only included RPC hit rates. The first 8 functions are dedicated to produce the TGraphs for the RPC
detector. The other function (the mega redundant lines 268-1273) produces every plot.
