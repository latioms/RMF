#il s'agit d'un code qui va renommer les fichiers en supprimant les chaines
#  de caracteres indesirables 
import os

def DeleteStrFile(chaine):
    os.chdir(os.getcwd())
    count = 0
    for file in os.listdir():
        if chaine in file:
            name = file
            new_name = name.replace(chaine, "")
            file_oldname = os.path.join(os.getcwd(), name)
            file_newname = os.path.join(os.getcwd(), new_name)
            os.rename(file_oldname, file_newname)
            count += 1
    txt = "{} fichier(s) rendu(s) ".format(count)
    print(txt)

def main():
    chaine = "Streaming"
    print("Voulez vous continuer avec la chaine par defaut (1) \n")
    print("Ou souhaitez vous la configurer ? (0) \n")
    choice = -1
    #Choix a faire
    while True:
        try:
            choice = int(input("Entrez votre Choix: "))
            if choice == 1 or choice == 0:
                break
            else:
                print("\n Choisissez uniquement 0 ou 1")

        except ValueError:
            print("\n Valeur Incorrect entrez juste des entiers")
    #execution de la procedure
    if choice == 1:
        DeleteStrFile(chaine)
    else:
        characters = input("\n Entrez la chaine a effacer: ")
        DeleteStrFile(characters)
    
    input("Appuyez une touche pour sortir")

if __name__ == "__main__":
        main()