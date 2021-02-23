def formatted_number(number):
    width = len(bin(number)[2:])
    for num in range(1,number+1):
        deci = str(num)
        octa = oct(num)[2:]
        hexa = hex(num)[2:]
        bina = bin(num)[2:]
        print(deci.ljust(width),octa.ljust(width),hexa.ljust(width),bina.ljust(width))
n = int(input())
formatted_number(n)