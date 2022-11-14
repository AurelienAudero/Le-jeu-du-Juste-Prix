#Initialisation
from random import randint #Importation de randint() pour pouvoir générer le prix aléatoirement
from time import time #Importation de time() et sleep() pour les fonctionnalités de temps limité
prix_trouve = False #Mise en place d'une variable permettant d'arrêter la boucle si le prix est trouvé
mode_choisi = "AUCUN" #Mise en place d'une variable permettant de redemander à l'utilisateur la difficulté tant qu'il ne l'as pas bien saisi

def choix_mode():
  print("\033[1mBienvenue sur le Jeu du Juste Prix !\n\033[0m")
  print(
    "\033[4mLes modes de jeux disponibles sont :\033[0m\n- Le mode Facile (avec un nombre d'essais illimités)\n- Le mode difficile (avec 10 essais pour trouver)\n- Le mode limité (avec 30 secondes pour trouver, essais illimités)\n- Le mode personnalisé (faites votre partie comme vous l'entendez)\n")
  
  return input("Quel difficulté choissisez-vous ? ").upper()

def prop_joueur():
  n = int(input("\nQuel prix proposez-vous ? "))
  return n

def comparaison(m,n):
  if n == m:
    return "="
  elif n < m:
    return "+"
  elif n > m:
    return "-"

def affichage(c):
  if c == "=":
    print("Félicitations ! Vous avez trouvé le juste prix !")
  elif c == "+":
    print("C'est plus !")
  elif c == "-":
    print("C'est moins !")

#Demande de la difficulté et répétition tant qu'il ne saisi pas bien la difficulté
while not((mode_choisi == "FACILE")) and not((mode_choisi == "DIFFICILE")) and not ((mode_choisi == "LIMITE")) and not ((mode_choisi == "PERSONNALISE")) :
  mode_choisi = choix_mode()

#Jeu en mode Facile
if mode_choisi == "FACILE":
  prix_ordi = randint(0,100) #Génération du prix aléatoirement
  coup_restant = -1 #Mise en place du nombre de coups maximal

  while prix_trouve == False: #Se répéte tant que le prix n'est pas trouvé
    prix_joueur = prop_joueur() #Demande et sauvegarde du prix entré par le joueur
    resultat = comparaison(prix_ordi, prix_joueur) #Compare le prix généré par la machine et le prix entré par le joueur
    if resultat == "=": #Si le prix est trouvé alors il affiche le résultat et arrête la boucle
      affichage(resultat)
      prix_trouve = True
    else: #Sinon il ne fait qu'afficher le résultat ("C'est plus !" ou "C'est moins !")
      affichage(resultat)

#Jeu en mode Difficile
if mode_choisi == "DIFFICILE":
  prix_ordi = randint(0,100) #Génération du prix aléatoirement
  coup_restant = 10 #Mise en place du nombre de coups maximal

  while (prix_trouve == False) and (coup_restant != 0): #Se répéte tant que le prix n'est pas trouvé et qu'il y a encore des coup(s) restant(s)
    prix_joueur = prop_joueur() #Demande et sauvegarde du prix entré par le joueur
    resultat = comparaison(prix_ordi, prix_joueur) #Compare le prix généré par la machine et le prix entré par le joueur
    if resultat == "=": #Si le prix est trouvé alors il affiche le résultat et arrête la boucle
      affichage(resultat)
      prix_trouve = True
    else: #Sinon il afficher le résultat et enleve 1 au nombre de coup(s) restant(s)
      affichage(resultat)
      coup_restant -= 1

#Jeu en mode Limité
if mode_choisi == "LIMITE":
  start = time() #Stockage du timestamp de départ
  temps_ecoule = 0 #Stockage du temps écoulé
  prix_ordi = randint(0,100) #Génération du prix aléatoirement
  coup_restant = -1 #Mise en place du nombre de coups maximal

  while (prix_trouve == False) and (temps_ecoule <= 30): #Se répéte tant que le prix n'est pas trouvé et que le timer n'as pas dépassé 30 secondes
    prix_joueur = prop_joueur() #Demande et sauvegarde du prix entré par le joueur
    resultat = comparaison(prix_ordi, prix_joueur) #Compare le prix généré par la machine et le prix entré par le joueur
    if resultat == "=": #Si le prix est trouvé alors il affiche le résultat et arrête la boucle
      affichage(resultat)
      prix_trouve = True
      temps_ecoule = time() - start #Mise à jour du timer
      print("Vous avez trouvé en" + str(round(temps_ecoule)) + " secondes.")
    else: #Sinon il ne fait qu'afficher le résultat ("C'est plus !" ou "C'est moins !")
      affichage(resultat)
      temps_ecoule = time() - start #Mise à jour du timer
      if temps_ecoule <= 30: #Evite d'afficher un nombre négatif pour le temps restant
        print("Il vous reste " + str(round(30 - temps_ecoule)) + " secondes.")

#Jeu en mode Personnalisé
if (mode_choisi == "PERSONNALISE") or (mode_choisi == "PERSONNALISÉ"):
  isTimer = None
  isCustomTime = None
  isTryCount = None
  isCustomTryCount = None
  isPriceGeneration = None

  while isTimer == None:
    temp = input("Souhaitez-vous un minuteur ? ").upper()
    if temp == "OUI":
      isTimer = True
    elif temp == "NON":
      isTimer = False
      temps_souhaite = 999
      temps_ecoule = 0
  
  if isTimer:
    while isCustomTime == None:
      temp = input("Souhaitez-vous chosir le temps ? ").upper()
      if temp == "OUI":
        isCustomTime = True
        temps_souhaite = float(input("Quel temps voulez-vous (en secondes) ? "))
      elif temp == "NON":
        isCustomTime = False

  while isTryCount == None:
    temp = input("Voulez-vous avoir un nombre d'essais limité ? ").upper()
    if temp == "OUI":
      isTryCount = True
    elif temp == "NON":
      isTryCount = False
      coup_restant = -1 #Mise en place du nombre de coups maximal

  if isTryCount:
    while isCustomTryCount == None:
      
      temp = input("Voulez-vous modifier le nombre d'essais ? (Il y en a 10 par défaut) ").upper()
      if temp == "OUI":
        isCustomTryCount = True
        coup_restant = int(input("Entrez le nombre d'essais que vous souhaitez : "))
      elif temp == "NON":
        isCustomTryCount = False
        coup_restant = 10 #Mise en place du nombre de coups maximal

  while isPriceGeneration == None:
    temp = input("Voulez-vous générer le prix automatiquement ? ").upper()
    if temp == "OUI":
      isPriceGeneration = True
      isCustomPriceGeneration = None
      while isCustomPriceGeneration == None:
        temp = input("Souhaitez-vous choisir l'intervalle de génération ? (entre 1€ et 100€ par défaut) ").upper()
        if temp == "OUI":
          isCustomPriceGeneration = True
          x = int(input("Choissisez la valeur la plus basse possible : "))
          y = int(input("Choissisez la valeur la plus haute possible : "))
          prix_ordi = randint(x,y) #Génération du prix aléatoirement
        elif temp == "NON":
          isCustomPriceGeneration = False
          prix_ordi = randint(0,100) #Génération du prix aléatoirement
    elif temp == "NON":
      isPriceGeneration = False
      prix_ordi = int(input("Choissisez le prix que vous souhaiter avoir à trouver : "))

  if isTimer:
    start = time() #Stockage du timestamp de départ
    temps_ecoule = 0 #Stockage du temps écoulé

  while (prix_trouve == False) and (temps_ecoule <= temps_souhaite) and (coup_restant != 0): #Se répéte tant que le prix n'est pas trouvé et que le timer n'as pas dépassé x secondes (défini par temps_souhaite)
    prix_joueur = prop_joueur() #Demande et sauvegarde du prix entré par le joueur
    resultat = comparaison(prix_ordi, prix_joueur) #Compare le prix généré par la machine et le prix entré par le joueur
    if resultat == "=": #Si le prix est trouvé alors il affiche le résultat et arrête la boucle
      affichage(resultat)
      prix_trouve = True
      if isTimer:
        temps_ecoule = time() - start #Mise à jour du timer
        print("Vous avez trouvé en" + str(round(temps_ecoule)) + " secondes.")
    else: #Sinon il ne fait qu'afficher le résultat ("C'est plus !" ou "C'est moins !")
      affichage(resultat)
      if isTimer:
        temps_ecoule = time() - start #Mise à jour du timer
        if temps_ecoule <= temps_souhaite: #Evite d'afficher un nombre négatif pour le temps restant
          print("Il vous reste " + str(round(temps_souhaite - temps_ecoule)) + " secondes.")
      if isTryCount:
        coup_restant -= 1

#Informe l'utilisateur qu'il a perdu si il a dépassé les 10 essais ou qu'il a mis trop de temps
if coup_restant == 0:
  print("\033[1m\033[31m\nVous avez perdu ! Vous avez fait trop d'essais !\033[0m")
elif temps_ecoule >= temps_souhaite:
  print("\033[1m\033[31m\nVous avez perdu ! Vous avez mis trop de temps !\033[0m")