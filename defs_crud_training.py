workouts = []

import random

def acessar_quarto_indice(nome_arquivo, delimitador=" "):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                elementos = linha.strip().split(delimitador)
                if len(elementos) >= 4:
                    yield elementos[3]
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception:
        print("Erro inesperado ao acessar os dados.")

def calcular_porcentagem(parte, total):
    try:
        porcentagem = (parte / total) * 100
        return porcentagem
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
        return 0
    except Exception:
        print("Erro inesperado ao calcular porcentagem.")
        return 0

def save_workout_data(filename="workout_data.txt"):
    try:
        with open(filename, "w") as file:
            for workout in workouts:
                line = f"{workout['id']},{workout['name']},{workout['date']},{workout['distance']},{workout['time']},{workout['localization']},{workout['weather']}\n"
                file.write(line)
    except Exception:
        print("Erro ao salvar os dados dos treinos.")

def read_workout_data(filename="workout_data.txt"):
    global workouts
    try:
        workouts = []
        with open(filename, "r") as file:
            for line in file:
                try:
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
                except ValueError:
                    print(f"Erro ao processar linha do arquivo: {line.strip()}")
    except FileNotFoundError:
        print("Erro: Arquivo de treinos não encontrado.")
    except Exception:
        print("Erro inesperado ao carregar os dados dos treinos.")

def create_workout(name, date, distance, time, localization, weather):
    try:
        new_workout = {
            "id": len(workouts) + 1,
            "name": name,
            "date": date,
            "distance": distance,
            "time": time,
            "localization": localization,
            "weather": weather
        }
        workouts.append(new_workout)
        print("Treino criado com sucesso!")
        save_workout_data()
    except Exception:
        print("Erro ao criar um novo treino.")

def read_workout():
    try:
        if not workouts:
            print("Sem treinos registrados!")
            return

        for i, workout in enumerate(workouts):
            print(f"Treino {i + 1}:\n  Nome: {workout['name']} \n  Data: {workout['date']} \n  Distância: {workout['distance']}KM \n  Tempo: {workout['time']} Minutos \n  Localização: {workout['localization']} \n  Clima: {workout['weather']}")
            print("-=" * 15)
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
    except ValueError:
        print("Erro: Entrada inválida para filtro.")
    except Exception:
        print("Erro inesperado ao ler treinos.")

def update_workout(id):
    try:
        for workout in workouts:
            if workout['id'] == id:
                print("1 - Atualizar Nome")
                print("2 - Atualizar Data")
                print("3 - Atualizar Distância")
                print("4 - Atualizar Tempo")
                print("5 - Atualizar Localização")
                print("6 - Atualizar Clima")
                resp = int(input("O que deseja atualizar? "))
                if resp == 1:
                    workout['name'] = input("Digite o novo nome: ")
                elif resp == 2:
                    workout['date'] = input("Digite a nova data: ")
                elif resp == 3:
                    workout['distance'] = float(input("Digite a nova distância: "))
                elif resp == 4:
                    workout['time'] = float(input("Digite o novo tempo: "))
                elif resp == 5:
                    workout['localization'] = input("Digite a nova localização: ")
                elif resp == 6:
                    workout['weather'] = input("Digite o novo clima: ")
                print("Treino atualizado com sucesso!")
                save_workout_data()
                return
        print("Treino não encontrado.")
    except ValueError:
        print("Erro: Entrada inválida para o campo.")
    except Exception:
        print("Erro inesperado ao atualizar o treino.")

def delete_workout(id):
    try:
        for i, workout in enumerate(workouts):
            if workout['id'] == id:
                del workouts[i]
                print("Treino deletado com sucesso!")
                save_workout_data()
                return
        print("Treino não encontrado.")
    except Exception:
        print("Erro inesperado ao deletar treino.")

def cal_calc():
    try:
        if not workouts:
            print("Sem treinos registrados! Por favor, adicione treinos primeiro.")
            return

        print("\nCalorias Queimadas:\n")
        print("-=" * 15)
        for workout in workouts:
            try:
                distance = workout['distance']
                calories = distance * 60

                print(f"Treino {workout['id']}: {workout['name']}")
                print(f"  Distância: {distance:.2f} km")
                print(f"  Estimativa de Calorias Queimadas: ~{calories:.2f} kcal")
                print("-=" * 15)
            except KeyError:
                print("Erro: Dados incompletos no treino.")
            except Exception:
                print("Erro inesperado ao processar treino.")
    except Exception:
        print("Erro inesperado ao calcular calorias.")

def workout_sugest():
    if not workouts:
        print("Nenhum treino registrado para sugerir.")
        return

    treino_aleatorio = random.choice(workouts)
    
    action = random.choice(["aumentar_distancia", "diminuir_tempo"])

    if action == "aumentar_distancia":
        nova_distancia = treino_aleatorio['distance'] + random.uniform(1, 2)
        print(f"\nSugestão de Treino: Aumente a distância para {nova_distancia:.2f} km.")
        print(f"Treino base: {treino_aleatorio['name']} - Distância: {treino_aleatorio['distance']} km - Tempo: {treino_aleatorio['time']} minutos.")
    else:
        novo_tempo = treino_aleatorio['time'] - random.uniform(1, 10)
        novo_tempo = max(0, novo_tempo)
        print(f"\nSugestão de Treino: Diminua o tempo para {novo_tempo:.2f} minutos.")
        print(f"Treino base: {treino_aleatorio['name']} - Distância: {treino_aleatorio['distance']} km - Tempo: {treino_aleatorio['time']} minutos.")