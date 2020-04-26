'''Jordan Souvigny
This program converts between decimal, binary, and hexadecimal number systems. It can convert
between any of the six unique combinations of those three number systems.
'''

def decToBinary(num): #converts decimal to binary code
    decNum = int(num)
    binaryString = ""
    if decNum == 0:
        binaryString = "0"
    else:
        while decNum>0:
            remDigit = decNum%2
            binaryString = str(remDigit) + binaryString
            decNum = decNum//2
    return int(binaryString)

def binToDec(num): #converts binary to decimal code
    binNum = int(num)
    convNum = 0
    expo = 0
    while binNum>0:
        digit = binNum % 10
        convNum = convNum + digit * (2**expo)
        binNum = binNum//10
        expo = expo+1
    return convNum

def decToHex(num): #converts decimal to hexadecimal code
    decNum = int(num)
    hexString = ""
    digitChar = ""
    if decNum == "0":
        hexString = "0"
        return hexString
    else:
        while decNum >0:
                remDigit = decNum%16
                if remDigit <10:
                    digitChar = str(remDigit)
                elif remDigit == 10:
                    digitChar = "A"
                elif remDigit == 11:
                    digitChar = "B"
                elif remDigit == 12:
                    digitChar = "C"
                elif remDigit == 13:
                    digitChar = "D"
                elif remDigit == 14:
                    digitChar = "E"
                elif remDigit == 15:
                    digitChar = "F"
                hexString = str(digitChar) + hexString
                decNum = decNum//16
    return hexString
    
def hexToDec(num): #coverts hexadecimal code to decimal code
    hexNum = num
    expo = len(num)-1
    hexDigit = 0
    convNum = 0
    hexConDict = {"0":0 ,"1": 1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    for digit in num:
        print(hexConDict.get(digit))
    for digit in num:
        hexDigit = hexConDict.get(digit)
        value = hexDigit*(16**expo)
        convNum = convNum+value
        expo = expo - 1
    return int(convNum)

def getNum():
    return input("Enter the number in the correct form which you would like to convert: ")

def getFroms():
    return str(input("Enter the starting number system: "))

def getTo():
    return str(input("Enter the number system you would like to convert to: "))

def printOut(froms,num,to,answer): #formats and prints output message
     output = "The conversion from {0} number {1} to {2} number is {3}."
     print(output.format(froms,num,to,answer))

def calculator(froms,num,to): #determines the algorithm to call and run
     if froms == "decimal" and to == "binary":
         return str(decToBinary(num))
     elif froms == "binary" and to == "decimal":
         return str(binToDec(num))
     elif froms == "decimal" and  to == "hexadecimal":
         return str(decToHex(num))
     elif froms == "hexadecimal" and to == "decimal":
         return str(hexToDec(num))
     elif froms == "binary" and to == "hexadecimal":
         return str(decToHex(binToDec(num))) #uses both methods to convert b/t binary and hexadecimal
     elif froms == "hexadecimal" and to == "binary":
         return str(decToBinary(hexToDec(num))) #uses both methods to convert b/t hexadecimal and binary
     else: #else handles input error cases
         return "[INPUT ERROR] Please enter either decimal, binary, or hexadecimal for the coversion options and a valid number."
    
def main():
    flag = "y"
    answer =""
    while flag == "y": #user can remain in the program until they say to exit
        froms = getFroms()
        num = getNum()
        to = getTo()
        answer = calculator(froms,num,to)
        printOut(froms, num, to, answer)
        flag = str(input("Would you like to continue - y/n?"))
    print("Thank you!")
    
main()

        
        
        
        
