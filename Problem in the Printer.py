while True:
    s=input()
    if s=="the end.": quit()

    else:
        for i in s:
            if i=="b": s=s.replace("b","6")
            if i=="g": s=s.replace("g","9")
            if i=="l": s=s.replace("l","1")
            if i=="o": s=s.replace("o","0")
            if i=="s": s=s.replace("s","5")
            if i=="z": s=s.replace("z","2")

            if i=="6": s=s.replace("6","b")
            if i=="9": s=s.replace("9","g")
            if i=="1": s=s.replace("1","l")
            if i=="0": s=s.replace("0","o")
            if i=="5": s=s.replace("5","s")
            if i=="2": s=s.replace("2","z")
    
        print(s)
