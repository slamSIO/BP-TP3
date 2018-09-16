#!/usr/bin/python3
# coding: utf-8

def estBissextile( annee ) :
	if annee % 400 == 0 or ( annee % 4 == 0 and annee % 100 != 0 ) :
		return True
	else :
		return False
		
		
		
		
def getNbJoursDansMois( mois , annee ) :
	pass
	# Recopier ici le code de l'exercice précédent
	
	
	

def estDateValide( jour , mois , annee ) :
	pass
	# Votre code ici




if __name__ == "__main__" :
	unJour = int( input( "Saisir le numéro du jour : " ) )
	unMois = int( input( "Saisir le numéro du mois : " ) )
	uneAnnee = int( input( "Saisir l'année : " ) )
	
	dateOk = estDateValide( unJour , unMois , uneAnnee )
	
	if dateOk == True :
		print( "La date est valide." )
	else :
		print( "La date n'est pas valide !" )
