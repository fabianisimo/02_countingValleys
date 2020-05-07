import random

def entrada_datos():
    n = random.randint(2,100)
    UD = ["U","D"]
    s = ""
    for i in range(n):
        a = random.randint(0,1)
        if a == 0:
            s = s + "U"
        else:
            s = s + "D"
    return [n,s]


entrada = entrada_datos()
n = entrada[0]
s = entrada[1]
print ("viaje total. ",s)
def countingValleys(n, s):
    valles = 0
    nivel = 0
    for i in range(n):
        if s[i] == "U":
            nivel = nivel + 1
            if nivel == 0:
                valles = valles + 1
        else:
            nivel = nivel - 1
    return valles

resultado = countingValleys(n, s)
print ("resultado: ",resultado)