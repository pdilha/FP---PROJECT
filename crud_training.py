import os
os.system("cls")

import defs_crud_training

workouts = []

while True:
    defs_crud_training.read_workout_data()
    print("=-=-= Menu Principal =-=-=")
    print("1 - Criar Atividade")
    print("2 - Ver Atividades")
    print("3 - Atualizar Atividades")
    print("4 - Deletar Atividades")
    print("5 - Gerenciar Metas")
    print("6 - Estimativa de Calorias Queimadas")
    print("7 - Sugestão de Treinos")
    print("8 - Sair do Programa")
    print("-=" * 15)
    
    try:
        user_opt = int(input("Função Desejada: "))
    except ValueError:
        print("Erro: Por favor, insira um número válido para a opção.")
        continue

    if user_opt == 1:
        print("-=" * 15)
        name = input("Nome da Atividade: ").strip()
        date = input("Data (DD/MM/AAAA): ").strip()
        while True:
            try:
                distance = float(input("Distância percorrida em KM: "))
                if distance < 0:
                    print("Erro: A distância não pode ser negativa.")
                    continue
                break
            except ValueError:
                print("Erro: Distância deve ser um número.")
        while True:
            try:
                time = float(input("Tempo de treino em minutos: "))
                if time <= 0:
                    print("Erro: O tempo deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Erro: Tempo deve ser um número.")
        localization = input("Localização: ").strip()
        weather = input("Clima: ").strip()
        print("-=" * 15)
        
        defs_crud_training.create_workout(name, date, distance, time, localization, weather)

    elif user_opt == 2:
        print("-=" * 15)
        try:
            defs_crud_training.read_workout()
        except Exception:
            print("Erro ao ler os treinos.")
    
    elif user_opt == 3:
        print("-=" * 15)
        defs_crud_training.workouts_numerate()
        while True:
            try:
                id = int(input("Número da Atividade: "))
                break
            except ValueError:
                print("Erro: Por favor, insira um número válido.")
        try:
            defs_crud_training.update_workout(id)
        except Exception:
            print("Erro ao atualizar treino.")
        print("-=" * 15)
    
    elif user_opt == 4:
        print("-=" * 15)
        defs_crud_training.workouts_numerate()
        while True:
            try:
                print("-=" * 15)
                id = int(input("Número da Atividade: "))
                break
            except ValueError:
                print("Erro: Por favor, Insira um Número Válido.")
        try:
            defs_crud_training.delete_workout(id)
        except Exception:
            print("Erro ao Deletar Atividade.")
    
    elif user_opt == 5:
        defs_crud_training.manage_goals()
    
    elif user_opt == 6:
        print("-=" * 15)
        try:
            defs_crud_training.cal_calc()
        except Exception:
            print("Erro ao calcular calorias.")
            
    elif user_opt == 7:
        print("-="  * 15)
        defs_crud_training.workout_sugest()
    
    elif user_opt == 8:
        print("-=" * 15)
        print("Saindo do Programa... Obrigado por usar nosso sistema")
        print("-=" * 15)
        break
    
    else:
        print("Opção Inválida. Tente Novamente")