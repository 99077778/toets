#Toets bootcamp Oskar van der Sluis


# Opdracht 1 (schrijf je antwoord als commentaar in een py file):

# a: Waarom is Visual Studio Code handiger voor software development dan bijvoorbeeld Notepad (kladblok)? Noem de voordelen!
# Het vult dingen aan automatisch en geeft errors weer, ook handig voor extensies zoals live server

# b: Waarom is het goed dat je de commits van jouw code pusht naar github.com?
# Zodat de docent het makkelijk kan bekijken en voor als je perongeluk je code verwijderd, dan staat het nog opgeslagen op github voor backup



#Opdracht 2:
# Maak het commentaar af.
#a = 5  # dit is een voorbeeld van het datatype:
#Integer

#b = 10.5  # dit is een voorbeeld van het datatype:
#Float

#c = "Hallo wereld" # dit is een voorbeeld van het datatype:
#String

 

#Opdracht 3:
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
# a = 5
# b = 10

# var = a

# a = b
# b = var

# Controleer met onderstaande code of de waarden correct zijn verwisseld

#print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen

 

#Opdracht 4:

# Los de problemen op (zonder exception handling).

# leeftijd = input("Hoe oud ben je?")
# leeftijd = int(leeftijd)
# print(f"Dan duurt het nog ongeveer {67 - leeftijd} jaar voordat je met pensioen mag!")

# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

 

#Opdracht 5: 
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
    # getal1 = 200
    # getal2 = 5
    # getal3 = 12

    # getal1 = int(getal1)
    # getal2 = int(getal2)
    # getal3 = int(getal3)


    # som = getal1 + getal2 + getal3

    # som = int(som)


    # antwoord = som# of de naam van je eigen functie.
    # print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

 

# Opdracht 6:
# # Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
        # AANTAL_GB = 20 # Aantal GB data in je bundel
        # AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
        # ONBEPERKT = False # test ook met True
        # aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
        # aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
        # if not ONBEPERKT and (aantal_minuten_gebeld > 200 or aantal_GB_internet > 20):
        #     print("Let op: je moet bijbetalen!")
        # else:
        #     print("Niet aan de hand gebruik je mobiel lekker verder!")



#Opdracht 7:
# Print onder elkaar de getallen 1-250 met max 2 regels code.

# var = range(1, 251)
# print(var)

 

#Opdracht 8:
# Gegeven is:

    # lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

    # # a: print een eenvoudig menu met de volgende layout:

    # # Onze menukaart:
    # # appel
    # # pannenkoek
    # # kiwi
    # # hamburger 

    # print("Onze menukaart: ")
    # for item in lijst_eten:
    #     print(item)

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. # Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). # test je code door extra eten toe te voegen met een nog langere naam.

# iets met len


 


#Opdracht 9:
# Schrijf een programma wat de gebruiker vraagt een cijfer in te voeren via de terminal.
# Dit blijf je herhalen totdat de gebruiker een getal tussen 0 en 10 heeft ingevoerd.
# Voert de gebruiker iets anders in dan een getal: geef een foutmelding.


# var = 0
# var = int(var)

# while var == 0:
#     try:
#         var = input('Vul een cijfer in van 0 - 10: ')
#         if 0 <= var <= 10:
#            break
#         else:
#            print("Voer een cijfer in tussen 0 en 10")
#     except ValueError:
#         print("Voer een cijfer in tussen 0 en 10")


 

# Opdracht 10:
# # repareer de volgende code:

    # MAX = 20
    # getal = input("Voer een getal in: ")

    # getal = int(getal)

    # if getal > MAX:
    #     input(f"Het getal is groter dan {MAX}")
    # elif getal < MAX:
    #     input(f"Het getal is kleiner dan {MAX}")
    # else:
    #     input(f"Het getal is gelijk aan {MAX}")