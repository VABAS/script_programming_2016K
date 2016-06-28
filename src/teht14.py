#!/usr/bin/python
#coding=UTF-8
def symbols(merkkijono):
	i=0;#Laskurimuuttuja
	for merkki in merkkijono:#Käydään annetun merkkijonon merkit läpi
		if merkki!="+" and merkki!="=":#Jos merkki ei ole + tai = se on kirjain
			if i-1>=0 and i+1<len(merkkijono):#Jos kirjaimen ympärillä on tilaa
				if merkkijono[i-1]!="+" and merkkijono[i+1]!="+":#Jos ympärillä olevat merkit eivät ole plussia se ei ole ympäröity
					return False;
			else:#Muutoin ei ole ympäröity
				return False;
		i+=1;#Lisätään laskurin arvoa yhdellä
	return True;#Jos kaikki testaukset kaikill kirjaimille onnistuivat merkkijono on ok ja palautetaan True
print symbols("++++")       # prints: True
print symbols("====")       # prints: True
print symbols("+=+=")       # prints: True
print symbols("++++=++++=") # prints: True
print symbols("a")          # prints: False, 'a' is not surrounded by + symbols at all!
print symbols("a+")         # prints: False, 'a' is surrounded by + only on the left side!
print symbols("+a")         # prints: False, 'a' is surrounded by + only on the right side!
print symbols("+a+")        # prints: True
print symbols("+a+====+b+") # prints: True
print symbols("+a+==x==+b+") # prints: False, 'x' is not surrounded by + symbols at all
