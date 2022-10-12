
from dataclasses import replace


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

def CheckBinary(string):
    if(string.count('0')+string.count('1')==len(string)):
        return True
    else:
        return False

def CheckHexa(string):
    try:
        int(string,16)
    except ValueError:
        return False
    return len(string) % 2 == 0


def CleanLine(line):
    list1 = line.replace("(","")
    list1 = list1.replace(")","")
    list1 = list1.split(",")
    return list1

def ToBinary(number, binary, decimal, hexa):
    if binary == True:
        return number
    elif hexa == True:
        result = bin(int(number, 16))
        return result
    elif decimal == True:
        num = bin(int(number)).replace("0b","")
        #print(num)
        #print(type(num))
        i = 0
        while len(num) < 8:
            num = "0" + num
            i+=1
        return num
    



def MOV(list, file):  #MOV (RealLine) -> ins basicas
    linea = list1[1].split(",")  
    if "(" in linea[0]: # #EJ: MOV (Lit),A
        linea[0] = linea[0].replace("(","")
        linea[0] = linea[0].replace(")","")
        pos1 = linea[0].isnumeric()
        pos2 = CheckBinary(linea[0])
        pos3 = CheckHexa(linea[0])
        if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
            num = linea[0]
            binary = ToBinary(num, pos2, pos1, pos3)
            if linea[1] == "A":
                file.write(line + "\n")
                file.write("0100111" + binary + "\n")
            elif linea[1] == "B":
                file.write(line + "\n")
                file.write("0101000" + binary + "\n")
        else:
            file.write(line + "\n")
            file.write("010101100000000" + "\n")


    elif "(" in linea[1] :   #EJ: MOV A,(Dir)
        linea[1] = linea[1].replace("(","")
        linea[1] = linea[1].replace(")","")
        pos1 = linea[1].isnumeric()
        pos2 = CheckBinary(linea[1])
        pos3 = CheckHexa(linea[1])
        if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
            num = linea[1]
            binary = ToBinary(num, pos2, pos1, pos3)
            if linea[0] == "B":
                file.write(line + "\n")
                file.write("0100110" + binary + "\n")
            elif linea[0] == "A":
                file.write(line + "\n")
                file.write("0100101" + binary + "\n")
        else: 
            if linea[0] == "A":
                file.write(line + "\n")
                file.write("010100100000000" + "\n")
            elif linea[0] == "B":
                file.write(line + "\n")
                file.write("010101000000000" + "\n")
                
    else:   # para abajo instrucciones basicas
        if len(linea) > 1:
            pos1 = linea[1].isnumeric()
            pos2 = CheckBinary(linea[1])
            pos3 = CheckHexa(linea[1])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[1]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[0] == "A":
                    file.write(line + "\n")
                    file.write("0000010" + binary + "\n")
                elif linea[0] == "B":
                    file.write(line + "\n")
                    file.write("0000011" + binary + "\n")
            else:
                if linea[0] == "A":
                    file.write(line + "\n")
                    file.write("000000000000000\n")
                elif linea[0] == "B":
                    file.write(line + "\n")
                    file.write("000000100000000\n")
    
def ADD(list, file):  
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej ADD A,(Dir)
        if "(" in linea[1]: # #EJ: ADD A,(Dir)
            linea[1] = linea[1].replace("(","")
            linea[1] = linea[1].replace(")","")
            pos1 = linea[1].isnumeric()
            pos2 = CheckBinary(linea[1])
            pos3 = CheckHexa(linea[1])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[1]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[0] == "A": # ADD A,(Dir)
                    file.write(line + "\n")
                    file.write("0101100" + binary + "\n")
                if linea[0] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("0101101" + binary + "\n")
            else:
                file.write(line + "\n") # SUB A,(B)
                file.write("010111000000000" + "\n")

        else: #XOR -> ins basicas
            if len(linea) > 1:
                pos1 = linea[1].isnumeric()
                pos2 = CheckBinary(linea[1])
                pos3 = CheckHexa(linea[1])
                if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                    num = linea[1]
                    binary = ToBinary(num, pos2, pos1, pos3)
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("0000110" + binary + "\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("0000111" + binary +" \n")
                else:
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("000010000000000\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("000010100000000\n")
            else:
                    pos1 = list[1].isnumeric()
    else: #Ej ADD (Dir)
        linea[0] = linea[0].replace("(","")
        linea[0] = linea[0].replace(")","")
        num = linea[0]
        pos1 = linea[0].isnumeric()
        pos2 = CheckBinary(linea[0])
        pos3 = CheckHexa(linea[0])
        binary = ToBinary(num,pos2, pos1, pos3 )
        file.write(line + "\n")
        file.write("0101111" + binary + "\n")
  
def SUB(list, file):  
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej ADD A,(Dir)
        if "(" in linea[1]: # #EJ: ADD A,(Dir)
            linea[1] = linea[1].replace("(","")
            linea[1] = linea[1].replace(")","")
            pos1 = linea[1].isnumeric()
            pos2 = CheckBinary(linea[1])
            pos3 = CheckHexa(linea[1])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[1]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[0] == "A": # ADD A,(Dir)
                    file.write(line + "\n")
                    file.write("0110000" + binary + "\n")
                if linea[0] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("0110001" + binary + "\n")
            else:
                file.write(line + "\n") # SUB A,(B)
                file.write("011001000000000" + "\n")

        else: #XOR -> ins basicas
            if len(linea) > 1:
                pos1 = linea[1].isnumeric()
                pos2 = CheckBinary(linea[1])
                pos3 = CheckHexa(linea[1])
                if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                    num = linea[1]
                    binary = ToBinary(num, pos2, pos1, pos3)
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("0001010" + binary + "\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("0001011" + binary +" \n")
                else:
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("000100000000000\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("000100100000000\n")
            else:
                    pos1 = list[1].isnumeric()
    else: #Ej ADD (Dir)
        linea[0] = linea[0].replace("(","")
        linea[0] = linea[0].replace(")","")
        num = linea[0]
        pos1 = linea[0].isnumeric()
        pos2 = CheckBinary(linea[0])
        pos3 = CheckHexa(linea[0])
        binary = ToBinary(num,pos2, pos1, pos3 )
        file.write(line + "\n")
        file.write("0110011" + binary + "\n")
  
def AND(list, file):  
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej ADD A,(Dir)
        if "(" in linea[1]: # #EJ: ADD A,(Dir)
            linea[1] = linea[1].replace("(","")
            linea[1] = linea[1].replace(")","")
            pos1 = linea[1].isnumeric()
            pos2 = CheckBinary(linea[1])
            pos3 = CheckHexa(linea[1])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[1]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[0] == "A": # ADD A,(Dir)
                    file.write(line + "\n")
                    file.write("0110100" + binary + "\n")
                if linea[0] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("0110101" + binary + "\n")
            else:
                file.write(line + "\n") # SUB A,(B)
                file.write("011011000000000" + "\n")

        else: #XOR -> ins basicas
            if len(linea) > 1:
                pos1 = linea[1].isnumeric()
                pos2 = CheckBinary(linea[1])
                pos3 = CheckHexa(linea[1])
                if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                    num = linea[1]
                    binary = ToBinary(num, pos2, pos1, pos3)
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("0001110" + binary + "\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("0001111" + binary +" \n")
                else:
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("000110000000000\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("000110100000000\n")
            else:
                    pos1 = list[1].isnumeric()
    else: #Ej ADD (Dir)
        linea[0] = linea[0].replace("(","")
        linea[0] = linea[0].replace(")","")
        num = linea[0]
        pos1 = linea[0].isnumeric()
        pos2 = CheckBinary(linea[0])
        pos3 = CheckHexa(linea[0])
        binary = ToBinary(num,pos2, pos1, pos3 )
        file.write(line + "\n")
        file.write("0110111" + binary + "\n")

def OR(list, file):  
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej ADD A,(Dir)
        if "(" in linea[1]: # #EJ: ADD A,(Dir)
            linea[1] = linea[1].replace("(","")
            linea[1] = linea[1].replace(")","")
            pos1 = linea[1].isnumeric()
            pos2 = CheckBinary(linea[1])
            pos3 = CheckHexa(linea[1])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[1]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[0] == "A": # ADD A,(Dir)
                    file.write(line + "\n")
                    file.write("0111000" + binary + "\n")
                if linea[0] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("0111001" + binary + "\n")
            else:
                file.write(line + "\n") # SUB A,(B)
                file.write("0111010000000" + "\n")

        else: #XOR -> ins basicas
            if len(linea) > 1:
                pos1 = linea[1].isnumeric()
                pos2 = CheckBinary(linea[1])
                pos3 = CheckHexa(linea[1])
                if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                    num = linea[1]
                    binary = ToBinary(num, pos2, pos1, pos3)
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("0010010" + binary + "\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("0010011" + binary +" \n")
                else:
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("001000000000000\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("001000100000000\n")
            else:
                    pos1 = list[1].isnumeric()
    else: #Ej ADD (Dir)
        linea[0] = linea[0].replace("(","")
        linea[0] = linea[0].replace(")","")
        num = linea[0]
        pos1 = linea[0].isnumeric()
        pos2 = CheckBinary(linea[0])
        pos3 = CheckHexa(linea[0])
        binary = ToBinary(num,pos2, pos1, pos3 )
        file.write(line + "\n")
        file.write("0111011" + binary + "\n")

def XOR(list, file):  
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej ADD A,(Dir)
        if "(" in linea[1]: # #EJ: ADD A,(Dir)
            linea[1] = linea[1].replace("(","")
            linea[1] = linea[1].replace(")","")
            pos1 = linea[1].isnumeric()
            pos2 = CheckBinary(linea[1])
            pos3 = CheckHexa(linea[1])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[1]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[0] == "A": # ADD A,(Dir)
                    file.write(line + "\n")
                    file.write("0111111" + binary + "\n")
                if linea[0] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("1000000" + binary + "\n")
            else:
                file.write(line + "\n") # SUB A,(B)
                file.write("100000100000000" + "\n")

        else: #XOR -> ins basicas
            if len(linea) > 1:
                pos1 = linea[1].isnumeric()
                pos2 = CheckBinary(linea[1])
                pos3 = CheckHexa(linea[1])
                if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                    num = linea[1]
                    binary = ToBinary(num, pos2, pos1, pos3)
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("0011010" + binary + "\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("0011011" + binary +" \n")
                else:
                    if linea[0] == "A":
                        file.write(line + "\n")
                        file.write("001100000000000\n")
                    elif linea[0] == "B":
                        file.write(line + "\n")
                        file.write("001100100000000\n")
            else:
                    pos1 = list[1].isnumeric()
    else: #Ej ADD (Dir)
        linea[0] = linea[0].replace("(","")
        linea[0] = linea[0].replace(")","")
        num = linea[0]
        pos1 = linea[0].isnumeric()
        pos2 = CheckBinary(linea[0])
        pos3 = CheckHexa(linea[0])
        binary = ToBinary(num,pos2, pos1, pos3 )
        file.write(line + "\n")
        file.write("1000010" + binary + "\n")


def NOT(list, file):   
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej NOT (Dir),A
        if "(" in linea[0]: # #EJ: ADD A,(Dir)
            linea[0] = linea[0].replace("(","")
            linea[0] = linea[0].replace(")","")
            pos1 = linea[0].isnumeric()
            pos2 = CheckBinary(linea[0])
            pos3 = CheckHexa(linea[0])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[0]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[1] == "A": #  (Dir),A
                    file.write(line + "\n")
                    file.write("0111100" + binary + "\n")
                if linea[1] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("0111101" + binary + "\n")

        else: #ADD -> ins basicas
            if linea[0] == "A" and linea[1] == "A":
                file.write(line + "\n")
                file.write("001010000000000\n")
            elif linea[0] == "A" and linea[1] == "B":
                file.write(line + "\n")
                file.write("001010100000000\n")
            elif linea[0] == "B" and linea[1] == "A":
                file.write(line + "\n")
                file.write("001011000000000\n")
            else:
                file.write(line + "\n")
                file.write("001011100000000\n")

    else: #Ej NOT (Dir)
        file.write(line + "\n")
        file.write("0111110000000" + "\n")

def SHL(list, file):   
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej NOT (Dir),A
        if "(" in linea[0]: # #EJ: ADD A,(Dir)
            linea[0] = linea[0].replace("(","")
            linea[0] = linea[0].replace(")","")
            pos1 = linea[0].isnumeric()
            pos2 = CheckBinary(linea[0])
            pos3 = CheckHexa(linea[0])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[0]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[1] == "A": #  (Dir),A
                    file.write(line + "\n")
                    file.write("1000011" + binary + "\n")
                if linea[1] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("1000100" + binary + "\n")

        else: #ADD -> ins basicas
            if linea[0] == "A" and linea[1] == "A":
                file.write(line + "\n")
                file.write("001110000000000\n")
            elif linea[0] == "A" and linea[1] == "B":
                file.write(line + "\n")
                file.write("001110100000000\n")
            elif linea[0] == "B" and linea[1] == "A":
                file.write(line + "\n")
                file.write("001111000000000\n")
            else:
                file.write(line + "\n")
                file.write("001111100000000\n")

    else: #Ej NOT (Dir)
        file.write(line + "\n")
        file.write("100010100000000" + "\n")

def SHR(list, file):   
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if len(linea) > 1: #Ej NOT (Dir),A
        if "(" in linea[0]: # #EJ: ADD A,(Dir)
            linea[0] = linea[0].replace("(","")
            linea[0] = linea[0].replace(")","")
            pos1 = linea[0].isnumeric()
            pos2 = CheckBinary(linea[0])
            pos3 = CheckHexa(linea[0])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[0]
                binary = ToBinary(num, pos2, pos1, pos3)
                if linea[1] == "A": #  (Dir),A
                    file.write(line + "\n")
                    file.write("1000110" + binary + "\n")
                if linea[1] == "B": # ADD B,(Dir)
                    file.write(line + "\n")
                    file.write("1000111" + binary + "\n")

        else: #ADD -> ins basicas
            if linea[0] == "A" and linea[1] == "A":
                file.write(line + "\n")
                file.write("010000000000000\n")
            elif linea[0] == "A" and linea[1] == "B":
                file.write(line + "\n")
                file.write("010000100000000\n")
            elif linea[0] == "B" and linea[1] == "A":
                file.write(line + "\n")
                file.write("010001000000000\n")
            else:
                file.write(line + "\n")
                file.write("010001100000000\n")

    else: #Ej NOT (Dir)
        file.write(line + "\n")
        file.write("100100000000000" + "\n")


def INC(list, file):   
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if "(" in linea[0]: # #EJ: ADD A,(Dir)
            linea[0] = linea[0].replace("(","")
            linea[0] = linea[0].replace(")","")
            pos1 = linea[0].isnumeric()
            pos2 = CheckBinary(linea[0])
            pos3 = CheckHexa(linea[0])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[0]
                binary = ToBinary(num, pos2, pos1, pos3)
                file.write(line + "\n")
                file.write("1001001" + binary + "\n")
            else:
                file.write(line + "\n")
                file.write("100101000000000" + "\n")
    #INC -> ins basicas
    else:
        file.write(line + "\n")
        file.write("010010000000000\n")
            
def RST(list, file):   
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if "(" in linea[0]: # #EJ: ADD A,(Dir)
            linea[0] = linea[0].replace("(","")
            linea[0] = linea[0].replace(")","")
            pos1 = linea[0].isnumeric()
            pos2 = CheckBinary(linea[0])
            pos3 = CheckHexa(linea[0])
            if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
                num = linea[0]
                binary = ToBinary(num, pos2, pos1, pos3)
                file.write(line + "\n")
                file.write("1001011" + binary + "\n")
            else:
                file.write(line + "\n")
                file.write("100110000000000" + "\n")

def CMP(list, file):
    linea = list1[1].split(",") # EJ A,B
    print("linea ", linea) 
    if "(" in linea[1]: #Ej CMP A,(Dir)
        linea[1] = linea[1].replace("(","")
        linea[1] = linea[1].replace(")","")
        pos1 = linea[1].isnumeric()
        pos2 = CheckBinary(linea[1])
        pos3 = CheckHexa(linea[1])
        if pos1 == True or pos2 == True or pos3 == True: #Ej INC (Dir)
            num = linea[1]
            binary = ToBinary(num, pos2, pos1, pos3)
            if linea[0] == "A":
                file.write(line + "\n")
                file.write("1010000" + binary + "\n")
            else:
                file.write(line + "\n")
                file.write("1010001" + binary + "\n")
        else: #CMP A,(B)
            file.write(line + "\n")
            file.write("101001000000000" + "\n")
    else:
        pos1 = linea[1].isnumeric()
        pos2 = CheckBinary(linea[1])
        pos3 = CheckHexa(linea[1])
        if pos1 == True or pos2 == True or pos3 == True: #Ej CMP A,Lit
            num = linea[1]
            binary = ToBinary(num, pos2, pos1, pos3)
            if linea[0] == "A":
                file.write(line + "\n")
                file.write("1001110" + binary + "\n")
            else:
                file.write(line + "\n")
                file.write("1001111" + binary + "\n")
        else: #CMP A,B
            file.write(line + "\n")
            file.write("100110100000000" + "\n")

        


        
        



def JMP(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1010011" + binary + "\n"))

def JEQ(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1010100" + binary + "\n"))

def JNE(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1010101" + binary + "\n"))

def JGT(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1010110" + binary + "\n"))

def JLT(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1010111" + binary + "\n"))

def JGE(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1011000" + binary + "\n"))

def JLE(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1011001" + binary + "\n"))

def JCR(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1011010" + binary + "\n"))

def JOV(list, file):
    num = int(list[1])
    #print(num)
    #print(" type num" , type(num))
    binary = ToBinary(num)
    file.write(line + "\n")
    file.write(("1011011" + binary + "\n"))

entry = open("cmp.txt", "r")
salida = open("salida.out", "w")
entrada = entry.readlines()

lenfile = len(entrada)
i = 0
while i <lenfile:
    RealLine = []
    line = entrada[i].strip() #linea de entrada
    list1 = line.split(" ")
    x = list1[1]
    #print("list1 " , list1)
    y = len(list1)
    if len(x) > 1:
        RealLine.append(list1[0]) #MOV
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
        SHR(RealLine, salida)         
    elif RealLine[0] == "INC":     
        INC(RealLine, salida)
    elif RealLine[0] == "RST":     
        RST(RealLine, salida)
    elif RealLine[0] == "CMP":     
        CMP(RealLine, salida)
    elif RealLine[0] == "JMP":     
        JMP(RealLine, salida)
    elif RealLine[0] == "JEQ":     
        JEQ(RealLine, salida)
    elif RealLine[0] == "JNE":     
        JNE(RealLine, salida)
    elif RealLine[0] == "JGT":     
        JGT(RealLine, salida)
    elif RealLine[0] == "JLT":     
        JLT(RealLine, salida)
    elif RealLine[0] == "JGE":     
        JGE(RealLine, salida)
    elif RealLine[0] == "JLE":     
        JLE(RealLine, salida)
    elif RealLine[0] == "JCR":     
        JCR(RealLine, salida)
    elif RealLine[0] == "JOV":     
        JOV(RealLine, salida)
       


    i+=1


entry.close()
salida.close()