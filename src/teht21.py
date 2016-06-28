#!/usr/bin/python
#coding=UTF-8
tama=(1,3,4);
dikti={"Eka":"Ensimmäinen","Toka":"Toinen"};
try:#Poista kommentointi riviltä jota haluat kokeilla
#	print tamaa;#Nostaa 'name error' poikkeuksen
#	print tama[4];#Nostaa 'index error' poikkeuksen
#	print dikti["eka"];#Nostaa 'key error' poikkeuksen
	print "Kaikki meni hienosti :O";
except NameError:#Nostetaan mikäli viitataan olemattomaan resurssiin
	print "Your variable/function doesn't exist!";
except IndexError:#Nostetaan mikäli yritetään lukea listasta/tuplesta olemattomalla indeksillä
	print "List index is out of range.";
except KeyError:#Nostetaan mikäli yritetään lukea olematonta dict key arvoa
	print "Dict key doesn't exist.";
