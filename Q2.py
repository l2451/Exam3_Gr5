import datetime
import locale
locale.setlocale(locale.LC_TIME,'')

def afficher_jours_examens(horaire_examen: dict) -> list[str]:
    """
    Cette fonction sert à extraire les jours de la semaines où il y a des examens
    :param horaire_examen: dictionnaire contenant les dates d'examens
    :return: une liste de jours de la semaine
    """
    # Est iterable -> on  utilise un for .. in pour parcourir le dictionnaire
    jours = [] # jour devrait être a l'exterieur

    for i in range(len(horaire_examen)):
        date = datetime.datetime.strptime(horaire_examen[i], "%Y-%m-%d")  #

        j = date.strftime("%Y-%m-%d")
        jours.append(j)
        return jours



if __name__ == '__main__':
    horaire_examen = {
        "math" : "10/12/2015",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    print("Les examens sont :", ", ".join(afficher_jours_examens(horaire_examen)))





