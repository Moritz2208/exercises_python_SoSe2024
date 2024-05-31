def vokon_zählen(wort):
    vokalen = "aeiou"
    wort_lower = wort.lower()
    
    bn = [i for i in wort_lower if i.isalpha()]
    vn = [k for k in wort_lower if k in vokalen]
    
    print(f"""Es gibt {len(vn)} Vokalen und {len(bn) - len(vn)} Konsonanten.""")
    
vokon_zählen("hi,&%/ Berlin!!")