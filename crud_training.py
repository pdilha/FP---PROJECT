import os
os.system("cls")

import defs_crud_training

lista_dist = []
workouts = []
meta = 0
nova_meta = 0
km_corridos = 0
k = 0
lista_mes = []

try:
    for quarto_indice in defs_crud_training.acessar_quarto_indice("workout_data.txt", ","):
        lista_dist.append(float(quarto_indice))
except (FileNotFoundError, ValueError):
    print("Erro ao carregar os dados do arquivo. Verifique se o arquivo existe e está no formato correto.")
    lista_dist = []

while True:
    defs_crud_training.read_workout_data()
    print("-=" * 15)
    print("1 - Criar Treino")
    print("2 - Ver Treino")
    print("3 - Atualizar Treino")
    print("4 - Deletar Treino")
    print("5 - Gerenciar metas")
    print("6 - Calorias queimadas")
    print("7 - Sugestão de Treinos")
    print("8 - Sair do Programa")
    print("-=" * 15)
    
    try:
        user_opt = int(input('Função desejada: '))
    except ValueError:
        print("Erro: Por favor, insira um número válido para a opção.")
        continue

    if user_opt == 1:
        print("-=" * 15)
        name = input("Nome do treino: ").strip()
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
                id = int(input("Número do treino: "))
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
                id = int(input("Número do treino: "))
                break
            except ValueError:
                print("Erro: Por favor, insira um número válido.")
        try:
            defs_crud_training.delete_workout(id)
        except Exception:
            print("Erro ao deletar treino.")
        print("-=" * 15)
    
    elif user_opt == 5:
        while True:
            print("-=" * 15)
            print('1 - Definir meta\n2 - Alterar meta\n3 - Verificar andamento da meta\n4 - Visualizar diário')
            print("-=" * 15)
            try:
                r = int(input('Função desejada: '))
            except ValueError:
                print("Erro: Por favor, insira um número válido.")
                continue
            
            if r == 1:
                if meta == 0:
                    try:
                        meta = float(input('\nDefina sua meta (em KM): '))
                        if meta <= 0:
                            print("Erro: A meta deve ser um número positivo.")
                            meta = 0
                        else:
                            print(f'\nOk, meta definida: {meta:.2f} Km ')
                    except ValueError:
                        print("Erro: A meta deve ser um número.")
                else:
                    print('\nMeta já definida!')
            elif r == 2:
                if meta == 0:
                    print('\nVocê precisa ter uma meta antes de alterá-la!')
                else:
                    try:
                        nova_meta = float(input('\nDefina sua nova meta: '))
                        if nova_meta <= 0:
                            print("Erro: A nova meta deve ser positiva.")
                        elif nova_meta == meta:
                            print('\nSua nova meta não pode ser igual à atual!')
                        else:
                            meta = nova_meta
                            print(f'\nOk, nova meta: {meta:.2f} Km')
                    except ValueError:
                        print("Erro: A nova meta deve ser um número.")
            elif r == 3:
                if meta != 0:
                    try:
                        soma = sum(lista_dist)
                        km_corridos = soma
                        resultado = defs_crud_training.calcular_porcentagem(km_corridos, meta)
                        print(f'Você correu {km_corridos} Km, equivalente a {resultado:.2f}% de sua meta.')
                    except ZeroDivisionError:
                        print("Erro: Meta não pode ser zero durante o cálculo.")
                else:
                    print('\nVocê precisa ter uma meta definida!')
            elif r == 4:
                if lista_dist:
                    for i, treino in enumerate(lista_dist, start=1):
                        print(f'Treino {i}: {treino} Km ')
                else:
                    print("Nenhum treino registrado.")
            else:
                print("Opção inválida.")
    
    elif user_opt == 6:
        print("-=" * 15)
        try:
            defs_crud_training.cal_calc("workout_data.txt")
        except Exception:
            print("Erro ao calcular calorias queimadas.")
            
    elif user_opt == 7:
        print("-="  * 15)
        defs_crud_training.workout_sugest()
    
    elif user_opt == 8:
        print("-=" * 15)
        print("Saindo do programa...")
        print("-=" * 15)
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 7.")
