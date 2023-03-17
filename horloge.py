from datetime import datetime,time, timedelta

updated = ( datetime.now() +
		timedelta( hours=0 )).strftime('%H:%M:%S')
print ("Il est : " + updated)

heures = None
minutes = None
secondes = None

def valide_heure(alarme):
    if len(alarme) != 8:
        return "Format temps invalide, veuillez réitérer votre saisie "
    else:
        if int(alarme[0:2]) > 24:
            return "Heure invalide, veuillez réitérer votre saisie "
        elif int(alarme[3:5]) > 59:
            return "Heure invalide, veuillez réitérer votre saisie "
        elif int(alarme[6:8]) > 59:
            return "Heure invalide, veuillez réitérer votre saisie "
        else:
            return "format valide"

def afficher_heure():
    global heures, minutes, secondes
    while True:
        changement_heure = input("Voulez vous régler l'heure ? ")
        if changement_heure.lower() == "oui":
            maintenant = input("Veuillez saisir l'heure sous format HH:MM:SS ")
            heures = maintenant[0:2]
            minutes = maintenant[3:5]
            secondes = maintenant[6:8]
            valide = valide_heure(maintenant)
            if valide != "format valide":
                print(valide)
            else:
                print ("Il est : " + maintenant)
                break
        elif changement_heure.lower() == "non":
            break
    
def actualise_sec():
    while True:
        heure_local = time.localtime()
        result = time.strftime('%H:%M:%S', heure_local)
        print(f'{result}', end='\r')
        time.sleep(1)

alarme = None 
def programation_alarme(alarme):
    global heures, minutes, secondes
    alarm_h = alarme[0:2]
    alarm_min = alarme[3:5]
    alarm_sec = alarme[6:8]
    if heures == None and minutes == None and secondes == None:
        while True:
            now = datetime.now()
            heure_actuel = now.strftime('%H')
            min_actuel = now.strftime('%M')
            sec_actuel = now.strftime('%S')
            print(heure_actuel + ":" +  min_actuel + ":" + sec_actuel, end='\r')
            if alarm_h == heure_actuel:
                if alarm_min == min_actuel:
                    if alarm_sec == sec_actuel:
                        print("C'est l'heure!")
                        break

    if heures != None and minutes != None and secondes != None:
        heures = int(heures)
        minutes = int(minutes)
        secondes = int(secondes)
        while True :
            if heures != alarm_h and minutes != alarm_min and secondes != alarm_sec:
                time.sleep(1)
                secondes += 1
                print(str(heures) + ":" +  str(minutes) + ":" + str(secondes), end='\r')
                if secondes == 60:
                    minutes += 1
                    secondes = 0
                if minutes == 60:
                    heures += 1
                    minutes = 0
                if heures == 24:
                    heures = 0
                    minutes = 0
                    secondes = 0
                if heures == int(alarm_h) and minutes == int(alarm_min) and secondes == int(alarm_sec):
                    print("C'est l'heure!")
                    break
            else:
                print("Erreur") 
                break 

def horloge(alarme):
    afficher_heure()

    while True:
        reponse_alarme = input("Voulez vous mettre une alarme ? ")
        if reponse_alarme.lower() == "oui":
            alarme = input("Votre demande d'alarme doit être sous format HH:MM:SS ")
            valide = valide_heure(alarme)
            if valide != "format valide":
                print(valide)
            else:
                print(f"Alarme programé pour {alarme}")
                break
        elif reponse_alarme.lower() == "non":
            break
           
    if alarme != None :
        programation_alarme(alarme)
    else:
        pass

horloge(alarme)