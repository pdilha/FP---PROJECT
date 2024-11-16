import os
os.system("clear")

import defs_crud_training

lista_dist=[]
workouts = []
meta=0
nova_meta=0
km_corridos=0
k=0
lista_mes=[]   

for quarto_indice in defs_crud_training.acessar_quarto_indice("workout_data.txt", ","):
    lista_dist.append(float(quarto_indice))

while True:
    defs_crud_training.read_workout_data()
    print("-=" * 15)
    print("1 - Criar Treino")
    print("2 - Ver Treino")
    print("3 - Atualizar Treino")
    print("4 - Deletar Treino")
    print("5 - Gerenciar metas")
    print("6 - Calorias queimadas")
    print("7 - Sair do Programa")
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
                    resultado= defs_crud_training.calcular_porcentagem (km_corridos, meta)
                    print(f'Você correu {km_corridos}Km, equivalente a {resultado:.2f}% de sua meta.')
                else:
                    print('\nVocê precisa ter uma meta definida!')
            elif r==4:
                for i in lista_dist:
                    k+=1
                    print(f'Treino {k}: {i} Km ')
    
    if user_opt == 7:
        print("-=" * 15)
        print("Saindo do programa...")
        print("-=" * 15)
        break