#!/usr/bin/python
#coding=UTF-8
i=0;#Laskurimuuttuja i
ii=9;#Apulaskuri ii
while i<10:#Pyöritetään silmukkaa niin pitkään kun laskuri on alle kymmenen
	print " "*ii+"A"*(i+1)*2;#Ensin tulostetaan ii määrä välilyöntejä ja sen jälkeen i+1 määrä A-kirjaimia
	i+=1;#Lisätään laskurin arvoa yhdellä
	ii-=1;#Ja vähennetään apulaskurin arvoa yhdellä
