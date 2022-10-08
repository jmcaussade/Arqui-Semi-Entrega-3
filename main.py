
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



entry = open("entrada.txt", "r")
salida = open("salida.out", "w")
entrada = entry.readlines()

lenfile = len(entrada)
i = 0
while i <lenfile:
    RealLine = []
    line = entrada[i].strip()
    list1 = line.split(" ")
    x = CleanLine(list1[1])
    y = len(list1)
    if len(x) > 1:
        RealLine.append(list1[0])
        RealLine.append(x[0]) #
        RealLine.append(x[1])
        print(RealLine)
    else:
        RealLine.append(list1[0])
        RealLine.append(x[0])
        print(RealLine)


    #print(x)
    """ ins = line[0:3]
    if ins == "MOV":
        print("MOV linea ",i, " \n")
        print(line, " \n") """
    #print(ins)
    salida.write(line)
    #salida.write(entrada[i])
    i+=1


entry.close()
salida.close()