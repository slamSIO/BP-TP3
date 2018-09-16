#!/usr/bin/python3
# coding: utf-8

def estBissextile( annee ) :
	if annee % 400 == 0 or ( annee % 4 == 0 and annee % 100 != 0 ) :
		return True
	else :
		return False




if __name__ == "__main__" :
	pass
	# Votre code ici
