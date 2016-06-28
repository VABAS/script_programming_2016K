#!/usr/bin/python
#coding=UTF-8
countrycodes=['fi','se','no'];#Maakoodit
codemap={'fi':'Finland','se':'Sweden','no':'Norway'};#Maiden nimet, indeksinä maakoodi
countries={#Maiden tiedot, indeksinä maan nimi
			'Finland':{'head honcho':('Juha Sipilä',54),'population':5.439},
			'Sweden':{'head honcho':('Stefan Lofven',58),'population':9.593},
			'Norway':{'head honcho':('Erna Solberg',54),'population':5.084}
};
for koodi in countrycodes:#Käydään maakoodilista läpi
	maa=codemap[koodi];#Tallennetaan maan nimi muuttujaan
	#Tulostetaan maan tiedot
	print maa,":\n\thead honcho: ",countries[maa]['head honcho'][0],", who is ",countries[maa]['head honcho'][1]," years old\n\tpopulation: ",countries[maa]['population']," million";
