import argparse


def Encriptar(Frase):
    Frase = Frase.upper()
    FraseEnc = '' #str vacio
    for letra in Frase: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                FraseEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
                            # if encontrado != True
            FraseEnc += letra
    print(FraseEnc)
    
def Desencriptar(Frase):
    Frase = Frase.upper()
    FraseDes = ''
    for letra in Frase:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                FraseDes += x #fraseEnc.append(x)
                encontrado = True
        if not encontrado: #if encontrado == False
            FraseDes += letra
    return FraseDes
    print(FraseDes)


#Cifrado César
#La letra más común del abc es la E
# A --> E, B ==> F, C --> G
# Ejemplo: CASA
# GEWE
abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
}