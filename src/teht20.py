#!/usr/bin/python
#coding=UTF-8
def division(l1,l2):
	try:#Kokeillaan jakaa ja tulostetaan osamäärä jos onnistutaan
		div=l1/l2;
		print div;
	except ZeroDivisionError:#Jos tulee nollallajako poikkeus, kerrotaan käyttäjälle ettei niin saa tehdä
		print "You tried to divide number",l1,"by zero. You can't do that! It's illegal in Finland...";
	except TypeError:
		print "One or both of supplied parameters are wrong type! To divide, I reguire numbers (int, float etc...). You know..."
division(10.0,4.0);#Tulostaa kaksi (2)
division(5,0);#Nostaa 'Division By Zero' poikkeuksen => Tulostaa varoituksen
division(5,"Eat this! You stupid program...");#Nostaa 'Type Error' poikkeuksen => Tulostaa varoituksen
try:#Kokeillaan onko viimeisessä kutsussa oikea määrä parametreja
	division(1,1,2);
except TypeError:#Ja siinä ei tietenkään ole, joten väännetään rautalangasta mikä mättää...
	print "You need to submit EXCATLY two (2) parameters for this function.";
