#!/usr/bin/python3
# coding: utf-8

import getpass

def seConnecterAdmin( login , password ) :
	pass
	# Votre code ici






if __name__ == "__main__" :
	nomConnexion = input( "Nom de connexion : " )
	motDePasse = getpass.getpass( "Mot de passe : " )

	connexionOk = seConnecterAdmin( nomConnexion , motDePasse )

	if connexionOk == True :
		print( "Connexion réussie." )
	else :
		print( "Connexion refusée." )
