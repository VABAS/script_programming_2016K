#!/usr/bin/python
#coding=UTF-8
def largest(lista):
	suurin=lista[0];#Tallennetaan listan ensimmäinen suurimmaksi
	for numero in lista:#Käydään listan elementit läpi
		if suurin<numero:#Jos listasta löytyy suurempi numero kuin mikä 'suurin' on
			suurin=numero;#Vaihdetaan suurin
	return suurin;#Palautetaan suurin
