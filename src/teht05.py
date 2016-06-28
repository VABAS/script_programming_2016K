#!/usr/bin/python
#coding=UTF-8
korkeus=10;
leveys=20;
i=0;#Laskurimuuttuja
while i<10:#Pyöritetään silmukkaa korkeuden verran
	if i is 0 or i is korkeus-1:#Jos ollaan ensimmäisellä tai viimeisellä kierroksella
		print "+"+"-"*leveys+"+";
	else:#Muutoin
		print "|"+"."*leveys+"|";
	i+=1;#Lisätään laskurin arvoa yhdellä
