"""
Titre : Logiciel Python projet
Date début : 5 novembre 2018
Auteurs : Groupe n°33 projet
"""
#####################################################################
"""
#Import des paquets
"""
import math

"""
#Définition des variables utilisées
"""
            #ptot = pression actuelle totale. Autrement dit la pression ambiante dans le lieu ou se trouve le séchoir.
            #Ta = Temperature de l'air ambiante (en Kelvin)
            #Ma = Masse molaire de l'air (sec)
            #Me = Masse molaire de l'eau
            #t = temps exprimé en heures de séchage

            #Trose = température de rosée
            #Hr est la température relatif
            #psat pression saturante à tTrose
            #tsky = Tsky :p
            #Ha est l'humidité absolue
            #Fd est le flux direct (W/m**2)
            #Fi Indirect est le flux indirect (W/m**2)

            #tempSerre la temperature de la serre (K)

            #Q est le debit d'air(m**3/s)

            #puissance e
h=0         #h est le coefficient d'échange de chaleur entre la surface et le toit
            #Fs est le flux d'énérgie produit par le sols par la loie des corps noirs
            #Ft est le flux d'énérgie produit par le toit par la loie des corps noirs
            #tempSurf est la temperature de la surface
            #tempToit est la temperature du toit
#####################################################################
"""
#Block Environnement
"""
Trose =

Hr = 

psat =

Tsky = Ta*(0.711 + (0.005 * Trosé) + (7,3 * (10 ** -5) * (Trosé ** 2)) + 0.013 * math.cos((2*pi*t)/24))**1/4

Ha = (Me/Ma) * ((Hr * psat)/(ptot-(Hr*psat)))



#####################################################################
def BlockEffetDeSerre(fluxD, fluxI, tempSerre,Q ):
#return Puissance





#####################################################################
"""
#Block Ventillation
"""
