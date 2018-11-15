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
Ma=0.8*28+0.2*32         #Ma = Masse molaire de l'air (sec)
Me= 18.016         #Me = Masse molaire de l'eau
            #t = temps exprimé en heures de séchage

            #Trose = température de rosée
            #Hr est la température relatif
            #psat pression saturante à tTrose
            #tsky = Tsky :p
            #Ha est l'humidité absolue
            #Fd est le flux direct (W/m**2)
            #Fi Indirect est le flux indirect (W/m**2)
            #Pe pression partiel de la vapeur

            #tempSerre la temperature de la serre (K)

            #Q est le debit d'air(m**3/s)

            #puissance e
            #h est le coefficient d'échange de chaleur entre la surface et le toit
            #Fs est le flux d'énérgie produit par le sols par la loie des corps noirs
            #Ft est le flux d'énérgie produit par le toit par la loie des corps noirs
            #tempSurf est la temperature de la surface
            #tempToit est la temperature du toit

#####################################################################

def BlockEnvironnement(Pto,Ta,t,ptot):
    psat =
    Fd=
    Hr =Pe/psat*100

    Trose = 373.15/(1-math.log(101325/ptot,math.e))

    Tsky = Ta*(0.711 + (0.005 * Trose) + (7,3 * (10 ** -5) * (Trose ** 2)) + 0.013 * math.cos((2*math.pi*t)/24))**1/4

    Ha = (Me/Ma) * ((Hr * psat)/(ptot-(Hr*psat)))

    Fi = 5.67*10**(-8)*Tsky

    return Fi,Ha,Fd



#####################################################################
def BlockEffetDeSerre(fluxD, fluxI, tempSerre,Q ):
#return Puissance





#####################################################################
"""
#Block Ventillation
"""
