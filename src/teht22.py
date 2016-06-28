#!/usr/bin/python
#coding=UTF-8
#thedict = [] # You can use existing dict as well
# ^-tuo on lista
thedict = {} #Tämä on dict
# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
	'''if listname in thedict:
		l = thedict[listname]
		print("%s already has %d elements." % (listname, len(l)))
	else:
		thedict[listname] = []
		print("Created %s." % listname)
		thedict[listname].append(element)
		print("Added %s to %s." % (element, listname))'''
	try:#Kokeillaan onnistuuke listaan 'listname' lisätä kenttä
		thedict[listname].append(element)
	except KeyError:#Jos ei onnistu syystä 'keyerror' tehdään lista ja kokeillaan uudelleen (ei suoriteta jos try onnistuu)
		thedict[listname] = []
		print("Created %s." % listname)
		thedict[listname].append(element)
	finally:#Lopuksi kerrotaan, että ollaan lisätty listaan (Suoritetaan viimeisenä joka tapauksessa)
		print("Added %s to %s." % (element, listname))

#Kokeilukutsut
add_to_list_in_dict(thedict,"lname","ihq");
add_to_list_in_dict(thedict,"mikko","ihq");
add_to_list_in_dict(thedict,"maukka","ihq");
add_to_list_in_dict(thedict,"lname","ihq");
print thedict;#Tulostetaan dicti niin nähdään mitä se sisältää
#thedict[listname].append(element) #Tämä pois
#print("Added %s to %s." % (element, listname)) #Ja tämä

