#!/usr/bin/python
#coding=UTF-8
def add(x,y):
	return x+y;
def sub(x,y):
	return x-y;
def multiply(x,y):
	return x*y;
def divide(x,y):
	return x/y;
def ask_numb():#Tällä kysytään yksittäinen float tyyppinen numero. Tätä käytetään neljästi, joten funktion käyttö säästää tilaa ja aikaa
        while True:#Pyöritetään kunnes saadaan kelvollinen vastaus
                try:
                        num=float(raw_input("Input number: "));#Jos float muunnos onnistuu on annettu sopivan tyyppinen arvo
                        break;#Poistutaan silmukasta
                except ValueError:#Muutoin annetaan virhe ja kysytään lukua uudelleen kun silmukka pyörähtää
                        print "Please input number!";
        return num;#Palautetaan numero

def vaihtoehdot():#Tätä käytetään vaihtoehtojen kerrontaan ja kokonaisluvun kysymiseen
	print "Select option";
	print "0) add";
	print "1) sub";
	print "2) multiply";
	print "3) divide";
	print "-1) quit";
	while True:#Pyöritetään kunnes saadaan kelvollinen vastaus
		try:
			vastaus=int(raw_input("Select: "));#Jos int muunnos onnistuu, on annettu sopivan tyyppinen vastaus
			break;#Poistutaan silmukasta
		except ValueError:#Muutoin annetaan virhe ja kysytään lukua uudelleen kun silmukka pyörähtää
			print "Please input integer!";
	return vastaus;#Palautetaan vastaus
while True:
	choice=vaihtoehdot();#Kutsutaan vastaus-funktiota ja tallenetaan sen antama arvo choice-muuttujaan
	if choice<0:#Jos on annettu alle nollan luku niin poistutaan ohjelmasta
		break;
	else:
		num1=ask_numb();
		num2=ask_numb();
		if choice==0:#Yhteenlasku
		        funk=add;
		elif choice==1:#Vähennyslasku
		        funk=sub;
		elif choice==2:#Kertolasku
		        funk=multiply;
		elif choice==3:#Jakolasku
		        funk=divide;
		try:#Kokeillaan virheiden varalta
			funk(num1,num2);
		except ZeroDivisionError:#Handlataan nollallajako virhe
			print "Error: Division by zero!";
		else:#Jos virheitä ei tullut, ilmoitetaan tulos
			print "The result is:",funk(num1,num2);
