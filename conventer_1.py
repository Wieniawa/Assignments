def binary_to_decimal(binary):
    decimal = 0
    while len(binary) > 1:
        licznik = 1
        for sign in binary:
            licznik *= 2
        decimal += licznik / 2
        if binary[0] == '1':
            binary = binary[1:]
        if binary[0] == '0':
            binary = binary[1:]
        if len(binary) == 1:
            if binary[-1] == '1':
                decimal += 1
    linia = '-'*(len(str(decimal)))
    print(" /"+linia+"-------\ ")
    print(" |",int(decimal),"|  10  |")
    print(" \ "+linia+"------/ ")


def decimal_to_binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    linia = '-'*(len(result))
    print(" /"+linia+"-------\ ")
    print(" |",result,"|  2 |")
    print(" \ "+linia+"------/ ")

def binary_validation(binary):
    for number in binary:
        if number != '0' and number != '1':
            print("Use only '1' or '0' !")
            main()
    binary_to_decimal(binary)


def main():
    while True:
        try:
            numbers = input('Type a number then space and choose system (2 for binary and 10 for decimal): ')
            split_numbers = numbers.split()
            number = int(split_numbers[0])
            system = split_numbers[1]
            binary = str(number)
            if system == '2':
                binary_validation(binary)
            elif system == '10':
                decimal_to_binary(number)
            else:
                print ('Wrong system!')

        except IndexError:
            print("ERROR! Please type --> number - space - 10 or 2 <-- !")
        except ValueError:
            print("ERROR! Use a numbers only!")

main()
