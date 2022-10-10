def ToBinary(number):
    num = bin(number).replace("0b","")
    print(num)
    print(type(num))
    i = 0
    while len(num) < 8:
        num = "0" + num
        i+=1
    print(num)
    
        
        



ToBinary(10)
            