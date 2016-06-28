#!/usr/bin/python
#coding=UTF-8
persons = ["alice", "bob", "craig", "dave", "elisabeth", "frank", "george"];
i=0;#Laskurimuuttuja
for person in persons:#Käydään taulukko läpi
	if i%2 is 0:#Jos solun indeksin jaettuna kahdella ei jätä jakojäännöstä, se on parillinen
		print str(i)+":"+person;#Tulostetaan tieto string(i) muuttaa indeksimuuttujan arvon merkkijonoksi
	i+=1;#Lisätään laskurimuuttujan arvoa yhdellä
