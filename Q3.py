
messages_gr5 = {
    "pseudo" : "IronCode",
    "messages" : ["Le monstre est au niveau 7", "Code 9 activé demain", "La réponse est 142"],
    "signatures" : ["fresea", "odivai", "nses14"]
}



"""pseudo_code
POUR ME SITUER DANS LE PROBLEME
message codé et message recus
le pseudo de la personne est IronCode( c,est la personne qui envoie le message
il doit recevoir le message de la part de l'agent secret 
chaque message a une signature en conservant seulement les deux avant derniere lettres
Ces signatures sont hachés         #14
trier les message pour confirmer que les message n'ont pas été modifier
afficher ce dont les signature sont valide aussi
donc il nous faudra deux fonction:



FONCTION (1) verifier les hach pour confirmer que les message n'ont pas été modifié.
      MA FONCTION PREND EN PARAMÈTRE LE MESSSAGE_GR5 QUI EST NOTRE DICTIONNAIRE DE MESSAGE
      indice:
      les signature sont des hach
      accedont alors dans les signatures
      lettre=14
      parcourir la lettre avec la boucle for pour 
      pour prendre 1 et 4 dans le mot et ensuite le comparer 
      a l'autre au message qui contient 1 et 4 #reponse c'est le dernier element de la liste conteneant  142
      qui est le message avec signature valide 
      ensuite print le code pour l'activer pour demain: CODE 9 ACTIVÉ Demain
      La reponse est 142
      -----------------------------------------------
      pour les message altérer.signatures non valides:
      le monstre est au niveau 7
      
      
      
        
      

L'autre FONCTION(2) doit 
trier les message pour afficher ceux dont la signature est valide
donc il faut parcourir tous les élement du message
 si message contient la reponse 124
 c,es le message valide
 on fait un trie message
 donc on reverse de la variable message
 reverse=TRUE la liste

 


"""
lettre=14
def verifier_hach(messages_gr5):
    """
    Cette fontion doit verifier FONCTION (1) verifier les
    hach pour confirmer
    don la signature correpondante doit avoir 14  comme  mot de hach
    que les message n'ont pas été modifié.
    :param messages_gr5:
    :return:
    """

    for ligne in messages_gr5:
        print(ligne)
        for element in ligne:
            print(element)
            if element[0]=="fresea":
                print(element[1])
            elif element[1]== "odivai":
                print(element[2])
            elif element[2]=="nses14":
                print(element[2])
    return







appel_verifier=verifier_hach(messages_gr5)
print(appel_verifier)

def message_valide(message_gr5):

   """
Cette FONCTION(2) doit
trier les message pour afficher ceu dont la signature est valide
"""
#non teminée fonction


