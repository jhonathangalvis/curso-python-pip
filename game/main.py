import random # se importa la funcion random para que que se elija de forma aleatoria el contenido de la variable

def choose_options():
    options=('piedra','papel','tijera')
    user_option=input('elije:piedra-papel-tijera : ')
    user_option=user_option.lower() #converti el ingreso de cualquier caracter a minuscula y mno tener problemas al comparar
    
    if not user_option in options:
        print(' !!!!!Opcion invalida!!!!\n')
        #continue #para brincar el resto del codigo si la opcion es invalida
        return None, None
    
    computer_option= random.choice(options) # uso randonm.choice para elegir una de las opciones de options
  
    print('User options => ', user_option)
    print('computer option=>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option==computer_option:
        print('empate')
    elif user_option=='piedra':
        if computer_option=='tijera':
            print('ganaste, piedra gana a tijera')
            user_wins+=1 # contador para veces ganadas
        else:
            print('perdiste, papel gana a piedra')
            computer_wins+=1 # contador para veces perdidas
    elif user_option=='papel':
        if computer_option=='piedra':
          print('ganaste, papel gana a piedra')
          user_wins+=1 # contador para veces ganadas
        else:
            print('perdiste, tijera gana a papel')
            computer_wins+=1 # contador para veces perdidas
    elif user_option=='tijera':
        if computer_option=='papel':
            print('ganaste, tijera gana a papel')
            user_wins+=1 # contador para veces ganadas
        else:
            print('perdiste, piedra gana a tijera')
            computer_wins+=1 # contador para veces perdidas
    return user_wins, computer_wins

def run_game():
    user_wins=0
    computer_wins=0
    rounds=1

    while True:
        
        print('*' * 13) #repetir un caracter n cantidad de veces
        print('-- ROUND --', rounds)
        print('*' * 13)
        
        print('user_wins', user_wins)
        print('computer_wins', computer_wins)
        
        rounds+=1
        
        user_option, computer_option = choose_options()    
    
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
            
        if computer_wins==2:
            print('El computador gano, fin del juego!')
            break
        if user_wins==2:
            print('Tu ganaste, fin del juego!')
            break
run_game()        