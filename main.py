
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

def ToBinary(number):
    num = bin(number).replace("0b","")
    print(num)
    print(type(num))
    i = 0
    while len(num) < 8:
        num = "0" + num
        i+=1
    return num



def MOV(list, file):  #MOV -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("000000000000000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("000000100000000\n")
        elif pos2 == True: #con literal
            num = int(list[2])
            print(num)
            print(" type num" , type(num))
            binary = ToBinary(num)
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0000010" + binary + "\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0000011" + binary + "\n")
    else:
            pos1 = list[1].isnumeric()

def ADD(list, file):  #ADD -> ins basicas
    if len(list) > 2:
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
            pos1 = list[1].isnumeric()

def SUB(list, file):  #SUB -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("000100000000000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("000100100000000\n")
        elif pos2 == True:
            num = int(list[2])
            print(num)
            print(" type num" , type(num))
            binary = ToBinary(num)
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0001010" + binary + "\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0001011" + binary + "\n")
    else:
            pos1 = list[1].isnumeric()

def AND(list, file):  #AND -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("000110000000000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("000110100000000\n")
        elif pos2 == True:
            num = int(list[2])
            print(num)
            print(" type num" , type(num))
            binary = ToBinary(num)
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0001110" + binary + "\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0001111" + binary + "\n")
    else:
            pos1 = list[1].isnumeric()

def OR(list, file):  #OR -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("001000000000000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("001000100000000\n")
        elif pos2 == True:
            num = int(list[2])
            print(num)
            print(" type num" , type(num))
            binary = ToBinary(num)
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0010010" + binary + "\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0010011" + binary + "\n")
    else:
            pos1 = list[1].isnumeric()

def XOR(list, file):  #XOR -> ins basicas
    if len(list) > 2:
        pos1 = list[1].isnumeric()
        pos2 = list[2].isnumeric()
        if pos2 == False:
            if list[1] == "A":
                file.write(line + "\n")
                file.write("001100000000000\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("001100100000000\n")
        elif pos2 == True:
            num = int(list[2])
            print(num)
            print(" type num" , type(num))
            binary = ToBinary(num)
            if list[1] == "A":
                file.write(line + "\n")
                file.write("0011010" + binary +"\n")
            elif list[1] == "B":
                file.write(line + "\n")
                file.write("0011011" + binary +"\n")
    else:
            pos1 = list[1].isnumeric()   

def NOT(list, file):   #NOT -> ins basicas
    if list[1] == "A" and list[2] == "A":
        file.write(line + "\n")
        file.write("001010000000000\n")
    elif list[1] == "A" and list[2] == "B":
        file.write(line + "\n")
        file.write("001010100000000\n")
    elif list[1] == "B" and list[2] == "A":
        file.write(line + "\n")
        file.write("001011000000000\n")
    else:
        file.write(line + "\n")
        file.write("001011100000000\n")

def SHL(list, file):   #SHL -> ins basicas
    if list[1] == "A" and list[2] == "A":
        file.write(line + "\n")
        file.write("001110000000000\n")
    elif list[1] == "A" and list[2] == "B":
        file.write(line + "\n")
        file.write("001110100000000\n")
    elif list[1] == "B" and list[2] == "A":
        file.write(line + "\n")
        file.write("001111000000000\n")
    else:
        file.write(line + "\n")
        file.write("001111100000000\n")

def SHR(list, file):   #SHL -> ins basicas
    if list[1] == "A" and list[2] == "A":
        file.write(line + "\n")
        file.write("001110000000000\n")
    elif list[1] == "A" and list[2] == "B":
        file.write(line + "\n")
        file.write("001110100000000\n")
    elif list[1] == "B" and list[2] == "A":
        file.write(line + "\n")
        file.write("001111000000000\n")
    else:
        file.write(line + "\n")
        file.write("001111100000000\n")

def INC(list, file):   #SHR -> ins basicas
    if list[1] == "B":
        file.write(line + "\n")
        file.write("010010000000000\n")

entry = open("entrada3.txt", "r")
salida = open("salida.out", "w")
entrada = entry.readlines()

lenfile = len(entrada)
i = 0
while i <lenfile:
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
        NOT(RealLine, salida)       
    elif RealLine[0] == "SHL":     
        SHL(RealLine, salida)         
    elif RealLine[0] == "SHR":     
        SHL(RealLine, salida)         
    elif RealLine[0] == "INC":     
        INC(RealLine, salida)
       


    i+=1


entry.close()
salida.close()