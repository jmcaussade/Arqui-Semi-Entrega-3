
Mov = ["A,B", "B,A", "A,Lit", "B,Lit",
"A,(Dir)", "B,(Dir)", "(Dir),A", "(Dir),A",
 "(Dir),B", "A,(B)", "B,(B)", "(B),A"] ##falta revisar Lit y (Dir)

Add = ["A, B", "B, A", "A, Lit", "B, Lit",
"A, (Dir)", "B, (Dir)", "A, (B)", "(Dir)"] ##falta revisar Lit y (Dir)

Sub = ["A, B", "B, A", "A, Lit", "B, Lit",
"A, (Dir)", "B, (Dir)", "A, (B)", "(Dir)"] ##falta revisar Lit y (Dir)

And = ["A, B", "B, A", "A, Lit", "B, Lit",
"A, (Dir)", "B, (Dir)", "A, (B)", "(Dir)"] ##falta revisar Lit y (Dir)

Or = ["A, B", "B, A", "A, Lit", "B, Lit",
"A, (Dir)", "B, (Dir)", "A, (B)", "(Dir)"] ##falta revisar Lit y (Dir)

Xor = ["A, B", "B, A", "A, Lit", "B, Lit", ##falta revisar Lit y (Dir)
"A, (Dir)", "B, (Dir)", "A, (B)", "(Dir)"]

Not = ["A, A", "A, B", "B, A", "B, B",  ##falta revisar (Dir)
 "(Dir), A", "(Dir), B", "(B)"]

Shl = ["A, A", "A, B", "B, A", "B, B",  ##falta revisar (Dir)
 "(Dir), A", "(Dir), B", "(B)"]

Shr = ["A, A", "A, B", "B, A", "B, B",  ##falta revisar (Dir)
 "(Dir), A", "(Dir), B", "(B)"]

Inc = ["B", "(Dir)", "(B)"]   ##falta revisar (Dir)

Rst = ["(Dir)", "(B)"]   ##falta revisar (Dir)

Cmp = ["A,B", "A, Lit", "B, Lit", "A, (Dir)",   ##falta revisar Lit y (Dir)
"B, (Dir)", "A, (B)"]

def CleanLine(line):
    list1 = line.replace("(","")
    list1 = list1.replace(")","")
    list1 = list1.split(",")
    return list1

def MOV(list, file):  #MOV -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0000000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0000001\n")
        elif pos2 == True:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0000010\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0000011\n")
    else:
            pos1 = list[1].isnumeric()

def ADD(list, file):  #ADD -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0000100\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0000101\n")
        elif pos2 == True:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0000110\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0000111\n")
    else:
            pos1 = list[1].isnumeric()

def SUB(list, file):  #SUB -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0001000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0001001\n")
        elif pos2 == True:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0001010\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0001011\n")
    else:
            pos1 = list[1].isnumeric()

def AND(list, file):  #AND -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0001100\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0001101\n")
        elif pos2 == True:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0001110\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0001111\n")
    else:
            pos1 = list[1].isnumeric()

def OR(list, file):  #OR -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0010000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0010001\n")
        elif pos2 == True:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0010010\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0010011\n")
    else:
            pos1 = list[1].isnumeric()

def XOR(list, file):  #XOR -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0011000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0011001\n")
        elif pos2 == True:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0011010\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0011011\n")
    else:
            pos1 = list[1].isnumeric()   

entry = open("entrada2.txt", "r")
salida = open("salida.out", "w")
entrada = entry.readlines()

lenfile = len(entrada)
i = 0
while i <lenfile -1:
    RealLine = []
    line = entrada[i].strip() #linea de entrada
    list1 = line.split(" ")
    print(list1)
    x = CleanLine(list1[1])
    y = len(list1)
    if len(x) > 1:
        RealLine.append(list1[0])
        RealLine.append(x[0]) 
        RealLine.append(x[1])
    else:
        RealLine.append(list1[0])
        RealLine.append(x[0])
        #print(RealLine)


    if RealLine[0] == "MOV":
        MOV(RealLine, salida)
    elif RealLine[0] == "ADD":
        ADD(RealLine, salida)
    elif RealLine[0] == "SUB":  
        SUB(RealLine, salida) 
    elif RealLine[0] == "AND":
        AND(RealLine, salida)    
    elif RealLine[0] == "OR":    
        OR(RealLine, salida)  
    elif RealLine[0] == "XOR":     
        XOR(RealLine, salida)    
    elif RealLine[0] == "NOT":     
        pass    
    elif RealLine[0] == "SHL":     
        pass   
    elif RealLine[0] == "SHR":     
        pass   
    elif RealLine[0] == "INC":     
        pass   
       

    
    #s = line +"\n"
    #salida.write(line + "\n")
    #salida.write(entrada[i])
    i+=1


entry.close()
salida.close()