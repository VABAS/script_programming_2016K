#!/usr/bin/python
#coding=UTF-8
import sys;
if len(sys.argv)>1:#Jos argumenrttilista on liian lyhyt (1. argumentti on suoritettavatiedosto indexillä 0 siis
	filename=sys.argv[1];
	try:#Jos tiedostoa ei voida avata
		filu=open(filename,"r");
	except IOError:#Kerrotaan käyttäjälle
		print "File named",filename,"not found";
	else:#Mutoin luetaan tiedosto kokonaan ja tulostetaan
		print filu.read();		
else:
	print "Not enough arguments. Usage:",sys.argv[0],"filename";
