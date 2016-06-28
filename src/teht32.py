#!/usr/bin/python
#coding=UTF-8
from teht31 import Student;
def read_student_data(file):
	try:
		tied=open(file,"r");
	except IOError:#Ilmoitetaan jos tiedostoa ei löydy
		print "File "+file+" not found";
	else:
		oppilaslista=[];
		oppilaat=tied.read().splitlines();#Luetaan jokainen rivi listan soluun
		for oppilas in oppilaat:#Käydään jokinen listan solu eli oppilas läpi
			oppilas=oppilas.split(";");#Oppilaan tiedot on eroteltu puolipilkuilla joten erotellaan tiedot listan soluiksi
			nimi=oppilas[0];
			ika=oppilas[1];
			tunnus=oppilas[2];
			kurssit=oppilas[3].split(",");#Viimeisessä solussa on kurssite eroteltuna pisteellä joten tehdään siitäkin oma lista
			temp=Student(nimi,ika,tunnus);#Väliaikainen olio
			for kurssi in kurssit:#Käydään kurssilista läpi ja lisätään ne yksitellen väliaikais-oliolle
				temp.add_course(kurssi);
			oppilaslista.append(temp);#Sisällytetään väliaikainen olio oppilaslistaan
		return oppilaslista;#Palautetaan oppilaslista
			
oppilaat=read_student_data("student-data.txt");
for oppilas in oppilaat:
	print oppilas.name+" "+oppilas.student_id;
