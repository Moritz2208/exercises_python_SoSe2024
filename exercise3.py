def steigung_funktion(liste):
    x1 = liste [0]
    y1 = liste [1]
    x2 = liste [2]
    y2 = liste [3]
    
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    steigung = delta_y / delta_x)
    
    if delta_x == 0:
        print("Die Steigung ist nicht definiert")
    else:
        steigung = delta_y / delta_x
        print(steigung)
steigung_funktion([4, 4, 8, 4])
