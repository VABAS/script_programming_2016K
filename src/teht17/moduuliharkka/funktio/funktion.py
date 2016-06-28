#coding=UTF-8
import country_data
def tama():
	for koodi in country_data.countrycodes:#Käydään maakoodilista läpi
		maa=country_data.codemap[koodi];#Tallennetaan maan nimi muuttujaan
		#Tulostetaan maan tiedot
		print maa,":\n\thead honcho: ",country_data.countries[maa]['head honcho'][0],", who is ",country_data.countries[maa]['head honcho'][1]," years old\n\tpopulation: ",country_data.countries[maa]['population']," million";
