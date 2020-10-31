def DecimalToBinary(x):
    BinaryNumber = ""
    while x>0:
        if x%2 == 0:
            BinaryNumber = "0 "+BinaryNumber
        else:
            BinaryNumber = "1 "+BinaryNumber
        x//=2
    return BinaryNumber

def main():
    x = int(input("Enter Decimal Number: ")) #x is assigned to input number here
    BinaryNumber = DecimalToBinary(x)
    print("Binary Number: ",BinaryNumber)
main()
