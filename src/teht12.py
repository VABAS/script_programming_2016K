#!/usr/bin/python
#coding=UTF-8
def sum2(numero):
	summa=0;#Summa on aluksi nolla
	i=0;#Laskurimuuttuja
	while i<=numero:#Pyöritetään niin pitkään että saavutetaan luku
		summa+=i;#Lisätään laskurin arvo summaan
		i+=1;#Lisätään laskurin arvoa yhdellä
	return summa;#Palautetaan summa
