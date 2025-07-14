valorOriginal = int(input())
valor = valorOriginal
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

while (valor > 0):
    if(valor >= 100):
        notas100 += 1
        valor -= 100
    elif (valor >= 50):
        notas50 += 1
        valor -= 50
    elif(valor >= 20):
        notas20 += 1
        valor -= 20
    elif(valor >= 10):
        notas10 += 1
        valor -= 10
    elif(valor >= 5):
        notas5 += 1
        valor -= 5
    elif(valor >= 2):
        notas2 += 1
        valor -= 2
    elif(valor >= 1):
        notas1 += 1
        valor -= 1

print(f"{valorOriginal}")
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")