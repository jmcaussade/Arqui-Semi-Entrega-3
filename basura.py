def ADD(list, file):  
    print("list ",list)  
    print("list1 ", list1)
    linea = list1[1].split(",")  
    print("linea###", linea)
    #ADD -> ins basicas
    if len(list) == 2:
        print("Aca")
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("000010000000000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("000010100000000\n")
        elif pos2 == True:
            num = int(list[2])
            print(num)
            print(" type num" , type(num))
            binary = ToBinary(num)
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0000110" + binary + "\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0000111" + binary +" \n")
    else:
        if "(" in list1[1] :   #EJ: ADD A,(Lit)
            print("linea 2",linea)
            linea[1] = linea[1].replace("(","")
            linea[1] = linea[1].replace(")","")
            print("linea 3",linea)
            x = linea[1]
            print("x ", x)
            y = x.isnumeric()
            if y == True:
                num = int(linea[1])
                binary = ToBinary(num)
            else:
                num = linea
            print("lineaaaaaa", linea)
            if linea[0] == "A":
                pos1 = linea[1].isnumeric()
                if pos1 == False: #EJ ADD A,(B)
                    file.write(line + "\n")
                    file.write("010111000000000" + "\n")
                else: #EJ ADD A,(Dir) -> ADD A,(5)
                    file.write(line + "\n")
                    file.write("0101100" + binary + "\n")
            elif linea[0] == "B":
                pos1 = linea[1].isnumeric()
                file.write(line + "\n")
                file.write("0101101" + binary + "\n")
            else:
                pos1 = linea[1].isnumeric()
                file.write(line + "\n")
                file.write("0101101" + binary + "\n")

            #pos1 = list[1].isnumeric()


def ADD(list, file):  #ADD -> ins basicas
    linea = list1[1].split(",")  
    print("list1", list1)
    t = list1[1].split(",")
    print(" t", t)
    print("linea", linea)
    if len(t) > 1:
        print("linea", linea[1])
        if "(" in linea[1] :   #EJ: ADD A,(Dir)
            linea[1] = linea[1].replace("(","")
            linea[1] = linea[1].replace(")","")
            pos1 = linea[0].isnumeric()
            pos2 = linea[1].isnumeric()
            if pos2 == False:
                if list[1] == "A": # ADD A,(B)
                    file.write(line + "\n")
                    file.write("000010000000000\n")
                """ elif list[1] == "B": #ADD B,(A) ## ERROR
                    file.write(line + "\n")
                    file.write("000010100000000\n") """
            elif pos2 == True: #Ej ADD A,(Dir)
                    linea[1] = linea[1].replace("(","")
                    linea[1] = linea[1].replace(")","")
                    x = linea[1]
                    y = x.isnumeric()
                    if y == True:
                        num = int(linea[1])
                        binary = ToBinary(num)
                    else:
                        num = linea[0]
                    if linea[0] == "A":
                        pos1 = linea[1].isnumeric()
                        if pos1 == False: #EJ ADD A,(B)
                            file.write(line + "\n")
                            file.write("010111000000000" + "\n")
                        else: #EJ ADD A,(Dir)
                            file.write(line + "\n")
                            file.write("0101100" + binary + "\n")
                    elif linea[0] == "B":
                        pos1 = linea[1].isnumeric()
                        if pos1 == True: #EJ ADD B,(Dir)
                            file.write(line + "\n")
                            file.write("0101101" + binary + "\n")
        else:

            num = int(linea[1])
            print(num)
            print(" type num" , type(num))
            binary = ToBinary(num)
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0000110" + binary + "\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0000111" + binary +" \n")
    else:
        t[0] = t[0].replace("(","")
        t[0] = t[0].replace(")","")
        binary = ToBinary(int(t[0]))
        file.write(line + "\n")
        file.write("0101111" + binary + "\n")