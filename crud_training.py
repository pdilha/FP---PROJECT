import os
os.system("cls")       

import defs_crud_training

while True:
    defs_crud_training.read_workout_data()
    print("-=" * 15)
    print("1 - Criar Treino")
    print("2 - Ver Treino")
    print("3 - Atualizar Treino")
    print("4 - Deletar Treino")
    print("5 - Sair do Programa")
    print("-=" * 15)
    
    user_opt = int(input(""))
    
    if user_opt == 1:
        print("-=" * 15)
        name = input("Nome do treino: ")
        date = input("Data: ")
        distance = float(input("Distância percorrida em KM: "))
        time = float(input("Tempo de treino em minutos: "))
        localization = input("Localização: ")
        weather = input("Clima: ")
        print("-=" * 15)
        
        defs_crud_training.create_workout(name, date, distance, time, localization, weather)
    
    if user_opt == 2:
        print("-=" * 15)
        defs_crud_training.read_workout()
    
    if user_opt == 3:
        print("-=" * 15)
        defs_crud_training.workouts_numerate()
        id = int(input("Número do treino: "))
        defs_crud_training.update_workout(id)
        print("-=" * 15)
    
    if user_opt == 4:
        print("-=" * 15)
        defs_crud_training.workouts_numerate()
        id = int(input("Número do treino: "))
        defs_crud_training.delete_workout(id)
        print("-=" * 15)
    
    if user_opt == 5:
        print("-=" * 15)
        print("Saindo do programa...")
        print("-=" * 15)
        break