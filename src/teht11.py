#!/usr/bin/python
#coding=UTF-8
def reverse(lista):
	lista2=[];#Uusi, tyhjä lista
	while len(lista)>0:#Pyöritetään kunnes alkuperäinen lista on tyhjä
		lista2.append(lista.pop());#Pullautetaan listan viimeinen pois ja tallennetaan se uuden listan perälle
	return lista2;#Palautetaan uusi lista
