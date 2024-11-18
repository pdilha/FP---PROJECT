import os
os.system ('clear')

lista_tempos=[]
tempo_min = 0

peso_kg = int(input('Insira seu peso: '))

def acessar_quinto_indice(nome_arquivo, delimitador=" "):
    with open('Proj FP/workout_data.txt', 'r') as arquivo:
        for linha in arquivo:
            elementos = linha.strip().split(delimitador)
            if len(elementos) >= 5:
                yield elementos[4]

for quinto_indice in acessar_quinto_indice("Proj FP/workout_data.txt", ","):
    lista_tempos.append(float(quinto_indice))

def calcular_calorias(peso, tempo, met=6):
    calorias = peso * met * tempo / 60
    return calorias

peso_kg = 70
tempo_min = 30
calorias_queimadas = calcular_calorias(peso_kg, tempo_min)
print(f"Você queimou aproximadamente {calorias_queimadas} calorias.")

        

