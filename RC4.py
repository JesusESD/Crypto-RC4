# Autor: Jesús Eduardo Salazar Domínguez

import fileinput

# intercambia valores de variables
def swap(x, y):
    aux = x
    x = y
    y = aux
    return x, y

# Conversión de los caracteres a su valor de Unicode
def toInt(text):
    intText = [ord(c) for c in text]
    return intText

# Algoritmo de Key-Scheduling
def KSA(key):
    keyLength = len(key)
    S = [*range(0, 256, 1)]
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keyLength]) % 256
        S[i], S[j] = swap(S[i], S[j])
    return S

# Algoritmo de Generación Pseudoaleatoria
# Genera una cadena del mismo tamaño que el texto en limpio
def PRGA(S, lenPlainText):
    keyStream = []
    i = 0
    j = 0
    for i in range(lenPlainText):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = swap(S[i], S[j])
        keyStream.append(S[(S[i] + S[j]) % 256])
    return keyStream

# Ejecución de RC4 empleando la llave y el tamaño del texto como parámetros
def RC4(key, intPlainText):
    # Ejecución de KSA y PRGA
    S = KSA(key)
    keyStream = PRGA(S, len(intPlainText))

    # Obtención del texto cifrado mediante la operación XOR (^)
    cipherText = []
    for i in range(len(keyStream)):
        num = keyStream[i] ^ intPlainText[i]
        cipherText.append(num)
	
    # Impresión del texto cifrado en formato hexadecimal
    cipherText = ''.join([format(c, '02X') for c in cipherText])
    print(cipherText)


def main():
    # Lectura del archivo de parámetros
    lines = []
    for line in fileinput.input():
        lines.append(line)

    # Almacenamiento del contenido del archivo en las variables correspondientes
    key = lines[0].strip()
    plainText = lines[1].strip()

    # Conversión de los caracteres a su código Unicode
    intKey = toInt(key)
    intPlainText = toInt(plainText)

    # Ejecución del algoritmo RC4
    RC4(intKey, intPlainText)


if __name__ == "__main__":
    main()
