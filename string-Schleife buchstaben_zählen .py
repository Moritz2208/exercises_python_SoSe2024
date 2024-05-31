def buchstaben_zählen(wort):
    liste = list(wort)
    buchstaben = [i for i in liste if i.isalpha()]
    print(len(buchstaben))
    
buchstaben_zählen("Hallo, Berlin")

