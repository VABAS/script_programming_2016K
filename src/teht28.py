#!/usr/bin/python
#coding=UTF-8
from random import randint;
numero=randint(0,20);#Randominumero väliltä 0-20 sisältäen ääripäät
print "++ Guessing Game ++\nGuess a number between 0 and 20 !";
guess_n=1;#Arvauslaskuri
while True:
	if guess_n>5:#Jos ollaan ohitettu viides arvays päätetään peli
		print "Game over, you lost! the correct number was",numero;
		break;#Poistutaan silmukasta
	elif guess_n>1:#Jos ollaan kuitenkin muussa kuin ensinmäisessä arvauksessa pyydetään yrittämään uudelleen
		print "Sorry, try again! ";
	guess=raw_input("Guess "+str(guess_n)+"/5:");#Kysytään käyttäjän arvaus
	try:#Tällä kokeillaan onko käyttäjän kirjoittama merkki kokonaisluku
		guess=int(guess);
	except ValueError:#Value-error tulee jos ei
		print "Not a number, try again";
	else:#Muutoin se on kokonaisluku (tai float tjsp... tällöin se pyöristetään alas päin)
		if guess in range(0,21):#Tarkastetaan onko käyttäjän kysymys oikealla välillä
			if guess==numero:#Käyttäjä on arvannut oikein
				print "Your guess was correct! Very good!"
			else:#Muutoin lisätään arvauslaskuria yhdellä
				guess_n+=1;
		else:#Kerrotaan jos ei oikealla välillä
			print "The guess should be between 0 and 20, try again";
