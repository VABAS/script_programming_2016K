#!/usr/bin/python
#coding=UTF-8
def vowels(merkkijono):
	vokaalit=('a','e','i','o','u');#Vokaalit tallennettu tupleen
	summa=0;#Summa on aluksi nolla
	for merkki in merkkijono:#Käydään merkkijonon jokainen merkki läpi
		for vokaali in vokaalit:#Käydään vokaalit läpi
			if merkki==vokaali:#Jos merkki on vokaali
				summa+=1;#Lisätään summaa yhdellä
				break;#Ja keskeytetään vokaalien läpikäynti
	return summa;#Palautetaan summa
