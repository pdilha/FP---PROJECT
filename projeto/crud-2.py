import random
import os
os.system("cls")

lista_dist=[]
workouts = []
meta=0
nova_meta=0
km_corridos=0
k=0
lista_mes=[]

def acessar_quarto_indice(nome_arquivo, delimitador=" "):
    with open('projeto\workout_data-1.txt', 'r') as arquivo:
        for linha in arquivo:
            elementos = linha.strip().split(delimitador)
            if len(elementos) >= 4:
                yield elementos[3]

def calcular_porcentagem(parte, total):
    porcentagem = (parte / total) * 100
    return porcentagem

def save_workout_data(filename="projeto\workout_data-1.txt"):
    with open("projeto\workout_data-1.txt", "w") as file:
        for workout in workouts:
            line = f"{workout['id']},{workout['name']},{workout['date']},{workout['distance']},{workout['time']},{workout['localization']},{workout['weather']}\n"
            file.write(line)

def read_workout_data(filename="projeto\workout_data-1.txt"):
    global workouts
    workouts = []
    with open("projeto\workout_data-1.txt", "r") as file:
        for line in file:
            id, name, date, distance, time, localization, weather = line.strip().split(',')
            workout = {
                    "id": int(id),
                    "name": name,
                    "date": date,
                    "distance": float(distance),
                    "time": float(time),
                    "localization": localization,
                    "weather": weather
                }
            workouts.append(workout)
            
def create_workout(name, date, distance, time, localization, weather):
    new_workout = {
        "id": len(workouts) + 1,
        "name": name,
        "date":  date,
        "distance": distance,
        "time": time,
        "localization": localization,
        "weather": weather
    } 
    workouts.append(new_workout)
    print("Treino criado com sucesso!")
    save_workout_data()

def read_workout():
    if not workouts:
        print("Sem treinos registrados!")
    for i, workout in enumerate(workouts):
        print(f"Treino {i + 1}:\n  Nome: {workout['name']} \n  Data: {workout['date']} \n  Distância: {workout['distance']}KM \n  Tempo: {workout['time']} Minutos \n  Localização: {workout['localization']} \n  Clima: {workout['weather']}")
    print()
    while True:
        print("Filtros: 1- Tempo | 2- Distância")
        filter_opt = int(input("Insira o filtro desejado ou 0 para retornar: "))
        if filter_opt == 0:
            break
        elif filter_opt == 1:
            time_filter_min = float(input("Insira o tempo mínimo de treino ou 0 caso não possua: "))
            time_filter_max = float(input("Insira o tempo máximo de treino ou 0 caso não possua: "))
            filtered_workouts = [
                workout for workout in workouts
                if (time_filter_min == 0 or workout["time"] >= time_filter_min) and (time_filter_max == 0 or workout["time"] <= time_filter_max)
            ]
            if not filtered_workouts:
                print("Nenhum treino encontrado!")
            else:
                for i, workout in enumerate(filtered_workouts):
                    print(f"Treino {i + 1}:\n  Nome: {workout['name']} \n  Data: {workout['date']} \n  Distância: {workout['distance']}KM \n  Tempo: {workout['time']} Minutos \n  Localização: {workout['localization']} \n  Clima: {workout['weather']}")
            print()
        elif filter_opt == 2:
            distance_filter_min = float(input("Insira a distância mínima de treino ou 0 caso não possua: "))
            distance_filter_max = float(input("Insira a distância máxima de treino ou 0 caso não possua: "))
            filtered_workouts = [
                workout for workout in workouts
                if (distance_filter_min == 0 or workout["distance"] >= distance_filter_min) and (distance_filter_max == 0 or workout["distance"] <= distance_filter_max)
            ]
            if not filtered_workouts:
                print("Nenhum treino encontrado!")
            else:
                for i, workout in enumerate(filtered_workouts):
                    print(f"Treino {i + 1}:\n  Nome: {workout['name']} \n  Data: {workout['date']} \n  Distância: {workout['distance']}KM \n  Tempo: {workout['time']} Minutos \n  Localização: {workout['localization']} \n  Clima: {workout['weather']}")
            print()
        
def update_workout(id):
    for i, workout in enumerate(workouts):
        if workout['id'] == id:
            print("1 - Atualizar Nome")
            print("2 - ATualizar Data")
            print("3 - Atualizar Distância")
            print("4 - Atualizar Tempo")
            print("5 - Atualizar Localização")
            print("6 - Atualizar Clima")
            resp = int(input("O que deseja atualizar? "))
            if resp == 1:
                novo_nome = input("Digite o novo nome: ")
                workout['name'] = novo_nome
            if resp == 2:
                nova_data = input("Digite o nova data: ")
                workout['date'] = nova_data
            if resp == 3:
                nova_distancia = input("Digite o nova distância: ")
                workout['distance'] = nova_distancia
            if resp == 4:
                novo_tempo = input("Digite o novo tempo: ")
                workout['time'] = novo_tempo
            if resp == 5:
                nova_localizacao = input("Digite o nova localização: ")
                workout['localization'] = nova_localizacao
            if resp == 6:
                novo_clima = input("Digite o novo clima: ")
                workout['weather'] = novo_clima
            print("Treino atualizado com sucesso!")
            return
    print("Treino não encontrado. Tente novamente!")

def delete_workout(id):
    for i, workout in enumerate(workouts):
        if workout['id'] == id:
            del workouts[i]
            print("Treino deletado com sucesso!")
            save_workout_data()
            return
    print("Treino não encontrado!")

def workouts_numerate():
    for i, workout in enumerate(workouts):
        print("Treinos: ")
        print(f"{i + 1} - {workout['name']}")       

for quarto_indice in acessar_quarto_indice("projeto\workout_data-1.txt", ","):
    lista_dist.append(float(quarto_indice))

while True:
    read_workout_data()
    print("-=" * 15)
    print("1 - Criar Treino")
    print("2 - Ver Treino")
    print("3 - Atualizar Treino")
    print("4 - Deletar Treino")
    print("5 - Sair do Programa")
    print("6 - Gerenciar metas")
    print("7 - Frequência Cardiaca")
    print("-=" * 15)
    
    user_opt = int(input('Função desejada: '))
    
    if user_opt == 1:
        print("-=" * 15)
        name = input("Nome do treino: ")
        date = input("Data: ")
        distance = float(input("Distância percorrida em KM: "))
        time = float(input("Tempo de treino em minutos: "))
        localization = input("Localização: ")
        weather = input("Clima: ")
        print("-=" * 15)
        
        create_workout(name, date, distance, time, localization, weather)
    
    if user_opt == 2:
        print("-=" * 15)
        read_workout()
    
    if user_opt == 3:
        print("-=" * 15)
        workouts_numerate()
        id = int(input("Número do treino: "))
        update_workout(id)
        print("-=" * 15)
    
    if user_opt == 4:
        print("-=" * 15)
        workouts_numerate()
        id = int(input("Número do treino: "))
        delete_workout(id)
        print("-=" * 15)
    
    if user_opt == 5:
        print("-=" * 15)
        print("Saindo do programa...")
        print("-=" * 15)
        break
    
    if user_opt == 6:
        while True:
            print("-=" * 15)
            print('1 - Definir meta\n2 - Alterar meta\n3 - Verificar andamento da meta\n4 - Vizualizar diário')
            print("-=" * 15)
            r=int(input('Função desejada: '))
            if r==1:
                if meta == 0:
                    meta=float(input('\nDefina sua meta: '))
                    print(f'\nOk, meta definida: {meta:.2f} Km ')
                else:
                    print('\nMeta já definida!')
            elif r==2:
                if meta==0:
                    print('\nVocê precisa ter uma meta antes de altera-la!')
                else:
                    nova_meta=float(input('\nDefina sua nova meta: '))
                    if nova_meta!=meta:
                        meta=nova_meta
                        print(f'\nOk, nova meta: {meta:.2f} Km')
                    else:
                        print('\nSua nova meta não pode ser igual a sua meta!')
            elif r==3:
                if meta != 0:
                    soma= sum(lista_dist)
                    km_corridos=soma
                    resultado= calcular_porcentagem (km_corridos, meta)
                    print(f'Você correu {km_corridos}Km, equivalente a {resultado:.2f}% de sua meta.')
                else:
                    print('\nVocê precisa ter uma meta definida!')
            elif r==4:
                for i in lista_dist:
                    k+=1
                    print(f'Treino {k}: {i} Km ')
    if user_opt == 7:
        numero_aleatorio = random.randint(110, 150)
        print(f'Sua frequencia cardiaca atual é: {numero_aleatorio} BPM')
