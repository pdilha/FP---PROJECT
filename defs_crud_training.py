workouts = []

import random
import os

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
                    print(f"Erro ao processar linha do arquivo.")
    except FileNotFoundError:
        print("Erro: Arquivo de atividades não encontrado.")
    except Exception:
        print("Erro inesperado ao carregar os dados das atividades.")

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
        print("Atividade criada com sucesso!")
        save_workout_data()
    except Exception:
        print("Erro ao criar uma nova atividade.")
        
def workouts_numerate():
    try:
        for i, workout in enumerate(workouts):
            print("Treinos: ")
            print(f"{i + 1}- {workout['name']}")  
    except ValueError:
        print(f"Erro de valor.")
    except KeyError:
        print(f"Erro de chave.")
    except Exception:
        print(f"Erro inesperado.")

def read_workout():
    try:
        if not workouts:
            print("Sem treinos registrados!")
            return

        for i, workout in enumerate(workouts):
            print(f"Atividade {i + 1}:\n  Nome: {workout['name']} \n  Data: {workout['date']} \n  Distância: {workout['distance']}KM \n  Tempo: {workout['time']} Minutos \n  Localização: {workout['localization']} \n  Clima: {workout['weather']}")
            print("-=" * 15)
        print()

        while True:
            print("Filtros: 1- Tempo | 2- Distância")
            filter_opt = int(input("Insira o Filtro Desejado ou 0 Para Retornar: "))
            if filter_opt == 0:
                break
            elif filter_opt == 1:
                time_filter_min = float(input("Insira o Tempo Mínimo de Atividade ou 0 Caso Não Possua: "))
                time_filter_max = float(input("Insira o Tempo Máximo de Atividade ou 0 Caso Não Possua: "))
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
                distance_filter_min = float(input("Insira a Distância Mínima de Atividade ou 0 Caso Não Possua: "))
                distance_filter_max = float(input("Insira a Distância Máxima de Atividade ou 0 Caso Não Possua: "))
                filtered_workouts = [
                    workout for workout in workouts
                    if (distance_filter_min == 0 or workout["distance"] >= distance_filter_min) and (distance_filter_max == 0 or workout["distance"] <= distance_filter_max)
                ]
                if not filtered_workouts:
                    print("Nenhuma atividade encontrada!")
                else:
                    for i, workout in enumerate(filtered_workouts):
                        print(f"Atividade {i + 1}:\n  Nome: {workout['name']} \n  Data: {workout['date']} \n  Distância: {workout['distance']}KM \n  Tempo: {workout['time']} Minutos \n  Localização: {workout['localization']} \n  Clima: {workout['weather']}")
                print()
    except ValueError:
        print("Erro: Entrada inválida para filtro.")
    except Exception:
        print("Erro inesperado ao ler atividades.")

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
                print("Atividade atualizada com sucesso!")
                save_workout_data()
                return
        print("Atividade não encontrada.")
    except ValueError:
        print("Erro: Entrada inválida para o campo.")
    except Exception:
        print("Erro inesperado ao atualizar o atividade.")

def delete_workout(id):
    try:
        for i, workout in enumerate(workouts):
            if workout['id'] == id:
                del workouts[i]
                print("Atividade Deletada com Sucesso!")
                save_workout_data()
                return
        print("Atividade não encontrada.")
    except Exception:
        print("Erro inesperado ao deletar atividade.")

def manage_goals():
    goals_file = "goals.txt"
    
    def define_goal():
        try:
            print("-=" * 15)
            distance_goal = float(input("Defina Sua Meta de Distância (em KM): "))
            time_goal = float(input("Defina Sua Meta de Tempo (em Min): "))
            print("-=" * 15)
            with open(goals_file, "w") as file:
                file.write(f"{distance_goal},{time_goal}\n")
            print("Meta Definida com Sucesso!")
        except ValueError:
            print("Erro: Entrada inválida. Insira números válidos para as metas.")
        except Exception:
            print("Erro inesperado ao definir a meta.")
    
    def update_goal():
        try:
            if not os.path.exists(goals_file):
                print("Nenhuma meta existente. Crie uma nova meta primeiro.")
                return
            
            with open(goals_file, "r") as file:
                line = file.readline().strip()
                distance_goal, time_goal = map(float, line.split(","))
            
            print(f"Meta atual: Distância: {distance_goal} km | Tempo: {time_goal} minutos")
            print("1 - Atualizar Meta de Distância")
            print("2 - Atualizar Meta de Tempo")
            option = int(input("Opção Desejada: "))
            
            if option == 1:
                distance_goal = float(input("Insira a nova meta de distância (em km): "))
            elif option == 2:
                time_goal = float(input("Insira a nova meta de tempo (em minutos): "))
            else:
                print("Opção inválida.")
                return
            
            with open(goals_file, "w") as file:
                file.write(f"{distance_goal},{time_goal}\n")
            print("Meta atualizada com sucesso!")
        except ValueError:
            print("Erro: Entrada inválida. Insira números válidos para as metas.")
        except Exception:
            print("Erro inesperado ao atualizar a meta.")
    
    def check_progress():
        try:
            if not os.path.exists(goals_file):
                print("Nenhuma meta definida. Crie uma nova meta primeiro.")
                return
            
            with open(goals_file, "r") as file:
                line = file.readline().strip()
                distance_goal, time_goal = map(float, line.split(","))
            
            read_workout_data()
            total_distance = sum(workout["distance"] for workout in workouts)
            total_time = sum(workout["time"] for workout in workouts)
            
            print("\nProgresso da Meta:")
            print(f"Meta de Distância: {distance_goal} km | Percorrido: {total_distance:.2f} km")
            print(f"Meta de Tempo: {time_goal} minutos | Realizado: {total_time:.2f} minutos")
            
            if total_distance >= distance_goal:
                print("Parabéns! Você alcançou sua meta de distância!")
            else:
                print(f"Faltam {distance_goal - total_distance:.2f} km para alcançar a meta de distância.")
            
            if total_time >= time_goal:
                print("Parabéns! Você alcançou sua meta de tempo!")
            else:
                print(f"Faltam {time_goal - total_time:.2f} minutos para alcançar a meta de tempo.")
        except Exception:
            print("Erro inesperado ao verificar o progresso da meta.")
    
    def view_goal_diary():
        try:
            if not os.path.exists(goals_file):
                print("Nenhuma meta definida. Crie uma nova meta primeiro.")
                return
            
            with open(goals_file, "r") as file:
                line = file.readline().strip()
                distance_goal, time_goal = map(float, line.split(","))
            
            print("\nDiário de Metas:")
            print(f"Meta de Distância: {distance_goal} km")
            print(f"Meta de Tempo: {time_goal} minutos")
        except Exception:
            print("Erro inesperado ao visualizar o diário de metas.")
    
    while True:
        print("-=" * 15)
        print("Gerenciamento de Metas:")
        print("1 - Definir Meta")
        print("2 - Atualizar Meta")
        print("3 - Verificar Progresso")
        print("4 - Visualizar Diário de Metas")
        print("5 - Voltar para o Menu Principal")
        print("-=" * 15)
        
        try:
            option = int(input("Opção Desejada: "))
            if option == 1:
                define_goal()
            elif option == 2:
                update_goal()
            elif option == 3:
                check_progress()
            elif option == 4:
                view_goal_diary()
            elif option == 5:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Escolha uma opção válida.")
        except Exception:
            print("Erro inesperado ao gerenciar metas.")

def cal_calc():
    try:
        if not workouts:
            print("Sem atividades registradas! Por favor, adicione atividades primeiro.")
            return

        print("\nCalorias Queimadas:\n")
        print("-=" * 15)
        for workout in workouts:
            try:
                distance = workout['distance']
                calories = distance * 60

                print(f"Atividade {workout['id']}: {workout['name']}")
                print(f"  Distância: {distance:.2f} km")
                print(f"  Estimativa de Calorias Queimadas: Aproximadamente {calories:.2f} kcal")
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