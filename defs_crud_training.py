workouts = []

def save_workout_data(filename="workout_data.txt"):
    with open("workout_data.txt", "w") as file:
        for workout in workouts:
            line = f"{workout['id']},{workout['name']},{workout['date']},{workout['distance']},{workout['time']},{workout['localization']},{workout['weather']}\n"
            file.write(line)

def read_workout_data(filename="workout_data.txt"):
    global workouts
    workouts = []
    with open("workout_data.txt", "r") as file:
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