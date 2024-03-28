# Name: Chase Prasad
# Title: Binary and Hex Converter

#converts hexadecimal characters into their decimal equivalents
def hex_char_decode(digit):
    #checks if the character is a number 0-9 and returns the int version of the digit
    if digit in "0123456789":
        return int(digit)
    else:
        #matches characters a through f with their respective numbers 10-15 and returns the number
        match digit:
            case 'a':
                return 10
            case 'b':
                return 11
            case 'c':
                return 12
            case 'd':
                return 13
            case 'e':
                return 14
            case 'f':
                return 15

#converts hexadecimal strings into their decimal equivalents
def hex_string_decode(hex):
    hex = hex.lower().lstrip("0x")
    deci = 0

    #goes through the hexadecimal string backwards and sends each character to the hex_char_decode function, of whose output it then multiplies by 16 to the power of the place value and adds to the deci variable
    for i in range(len(hex) - 1, -1, -1):
        deci += hex_char_decode(hex[i]) * 16 ** (len(hex) - 1 - i)
    
    return deci

#converts binary strings into their decimal equivalents
def binary_string_decode(binary):
    binary = binary.lstrip("0b")
    deci = 0

    #goes through the binary string backwards and multiplies each digit by 2 to the power of the place value and adds to the deci variable
    for i in range(len(binary) - 1, -1, -1):
        deci += int(binary[i]) * 2 ** (len(binary) - 1 - i)
    
    return deci

#converts binary strings into their hexadecimal equivalents
def binary_to_hex(binary):
    binary = binary.lstrip("0b")
    #first converts the binary string into its decimal equivalent using the binary_string_decode function to make the conversion easier
    deci = binary_string_decode(binary)
    digit = 1
    hexString = ""

    #mods the decimal equivalent by 16 and matches the remainder to its hexadecimal equivalent, then adds it to a string to return
    while digit > 0:
        digit = deci % 16
        deci //= 16
        
        if str(digit) in "0123456789":
            hexString += str(digit)
        else:
            match digit:
                case 10:
                    hexString += 'A'
                case 11:
                    hexString += 'B'
                case 12:
                    hexString += 'C'
                case 13:
                    hexString += 'D'
                case 14:
                    hexString += 'E'
                case 15:
                    hexString += 'F'
    
    #reverses the string for the proper order and removes the trailing 0
    return hexString.rstrip('0')[::-1]

def main():
    choice = 0

    while choice != 4:
        #displays menu and asks user to enter menu choice
        choice = int(input("Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n\nPlease enter an option: "))

        #matches user choice to proper output
        match choice:
            case 1:
                numString = input("Please enter the numeric string to convert: ")
                print(f"Result: {hex_string_decode(numString)}\n")
            case 2:
                numString = input("Please enter the numeric string to convert: ")
                print(f"Result: {binary_string_decode(numString)}\n")
            case 3:
                numString = input("Please enter the numeric string to convert: ")
                print(f"Result: {binary_to_hex(numString)}\n")

if __name__ == "__main__":
    main()