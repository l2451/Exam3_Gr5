import pytest
import datetime
import locale
locale.setlocale(locale.LC_TIME,'')


from Q2 import afficher_jours_examens,horaire_examen

def test_afficher_math():
    resultat0 = "math"
    afficher_math=afficher_jours_examens(horaire_examen,)
    resultat0="math"
    assert afficher_math==resultat0

def test_afficher_math():
    resultat1 = "anglais"
    afficher_anglais=afficher_jours_examens(horaire_examen)
    assert afficher_anglais==resultat1

def test_afficher_math():
    resultat2 = "français"
    afficher_français=afficher_jours_examens(horaire_examen)
    assert afficher_français==resultat2

def test_afficher_horraire_exemen():
    horaire_examen={
        "math" : "10/12/2015",
        "anglais" : "12/12/2025",
        "français" : "15/12/2025"
    }
    afficher_3=afficher_jours_examens(horaire_examen)
    assert afficher_3==horaire_examen


