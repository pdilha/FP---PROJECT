workouts = []

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

def read_workout():
    if not workouts:
        print("Sem treinos registrados!")
    for i, workout in enumerate(workouts):
        print(f"Treino {i + 1}:\n Nome: {workout["name"]} \n Data: {workout["date"]} \n Distância: {workout["distance"]}KM \n Tempo: {workout["time"]} \n Localização: {workout["localization"]} \n Clima: {workout["weather"]}")

def update_workout(id):
    for workout in workouts:
        if workout["id"] == id:
            print("1 - Atualizar Nome")
            print("2 - ATualizar Data")
            print("3 - Atualizar Distância")
            print("4 - Atualizar Tempo")
            print("5 - Atualizar Localização")
            print("6 - Atualizar Clima")
            resp = int(input("O que deseja atualizar? "))
            if resp == 1:
                novo_nome = input("Digite o novo nome: ")
                workout["name"] = novo_nome
            if resp == 2:
                nova_data = input("Digite o nova data: ")
                workout["date"] = nova_data
            if resp == 3:
                nova_distancia = input("Digite o nova distância: ")
                workout["distance"] = nova_distancia
            if resp == 4:
                novo_tempo = input("Digite o novo tempo: ")
                workout["time"] = novo_tempo
            if resp == 5:
                nova_localizacao = input("Digite o nova localização: ")
                workout["localization"] = nova_localizacao
            if resp == 6:
                novo_clima = input("Digite o novo clima: ")
                workout["weather"] = novo_clima
            print("Treino atualizado com sucesso!")
            return
    print("Treino não encontrado. Tente novamente!")

def delete_workout(id):
    for i, workout in enumerate(workouts):
        if workout["id"] == id:
            del workouts[i]
            print("Treino deletado com sucesso!")
            return
    print("Treino não encontrado!")

while True:
    print("1 - Criar Treino")
    print("2 - Ver Treino")
    print("3 - Atualizar Treino")
    print("4 - Deletar Treino")
    
    resp = int(input(""))
    
    if resp == 1:
        name = input("Nome do treino: ")
        date = input("Data: ")
        distance = float(input("Distância percorrida em KM: "))
        time = float(input("Tempo de treino: "))
        localization = input("Localização: ")
        weather = input("Clima: ")
        
        create_workout(name, date, distance, time, localization, weather)
    
    if resp == 2:
        read_workout()
    
    if resp == 3:
        id = int(input("ID do treino: "))
        update_workout(id)