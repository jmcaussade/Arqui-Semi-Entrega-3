MDic = ["MOV A,B", "MOV B,A", "MOV A,Lit", "MOV B,Lit",
"MOV A,(Dir)", "MOV B,(Dir)", "MOV (Dir),A", "MOV (Dir),A",
"MOV (Dir),B", "MOV A,(B)", "MOV B,(B)", "MOV (B),A", "ADD A,B", "ADD B,A", "ADD A,Lit", 
"ADD B,Lit","ADD A,(Dir)", "ADD B,(Dir)", "ADD A,(B)", "ADD (Dir)", 
"ADD A,1", "ADD B,1", "SUB A,1", "SUB B,1", "CMP A,1", "CMP B,1", "CALL Dir", "RET"
"SUB A,B", "SUB B,A", "SUB A,Lit", "SUB B,Lit","SUB A,(Dir)", "SUB B,(Dir)",
"SUB A,(B)", "SUB (Dir)", "AND A,B", "AND B,A", "AND A,Lit", "AND B,Lit",
"AND A,(Dir)", "AND B,(Dir)", "AND A,(B)", "AND (Dir)", "OR A,B", "OR B,A", 
"OR A,Lit", "OR B,Lit", "OR A,(Dir)", "OR B,(Dir)", "OR A,(B)", "OR (Dir)", 
"XOR A,B", "XOR B,A", "XOR A,Lit", "XOR B,Lit", "A,(Dir)", "B,(Dir)", "A,(B)",
"(Dir)", "NOT A,A", "NOT A,B", "NOT B,A", "NOT B,B",  "NOT (Dir),A", "NOT (Dir),B",
"NOT (B)", "SHL A,A", "SHL A,B", "SHL B,A", "SHL B,B",  "SHL (Dir),A", 
"SHL (Dir),B", "SHL (B)", "SHR A,A", "SHR A,B", "SHR B,A", "SHR B,B",  
"SHR (Dir),A", "SHR (Dir),B", "SHR (B)", "INC B", "INC (Dir)", "INC (B)", 
"RST (Dir)", "RST (B)", "CMP A,B", "CMP A,Lit", "CMP B,Lit", "CMP A,(Dir)",
"CMP B,(Dir)", "CMP A,(B)", "JMP Dir", "JEQ Dir", "JNE Dir", "JGT Dir",
"JLT Dir", "JGE Dir", "JLE Dir", "JCE (Dir)", "JOV Dir",
"PUSH A", "PUSH B", "POP A", "POP B"]

testlist = ["MOV A,%d"]

#print(testlist, % (2))
print(testlist[0] % (2))

file = open("salida.txt", "w")
h = len(MDic)-1
i = 0
while i<len(MDic):
    r = 0
    if i == 0:
        r = MDic[i].replace(" ","")
        r = '[' + '"' + r + '"' + ',' 
        file.write(r)
    elif i == h:
        r = MDic[i].replace(" ","")
        r = '"' + r + '"' + ']' 
        file.write(r)
    else:
        r = MDic[i].replace(" ","")
        r = '"' + r + '"' + ',' 
        file.write(r)
    i+=1

