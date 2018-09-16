#!/usr/bin/python3
# coding: utf-8

def estBissextile( annee ) :
	if annee % 400 == 0 or ( annee % 4 == 0 and annee % 100 != 0 ) :
		return True
	else :
		return False





def getNbJoursDansMois( mois , annee ) :
	pass
	# Votre code ici

if __name__ == "__main__" :
	unMois = int( input( "Saisir le numéro du mois : " ) )
	uneAnnee = int( input( "Saisir l'année : " ) )
	
	nbJours = getNbJoursDansMois( unMois , uneAnnee )
	
	if nbJours != -1 :
		print( "Le mois" , unMois , "de l'année" , uneAnnee , "compte" , nbJours , "jours." )
	else :
		print( "Mois inconnu !" )
