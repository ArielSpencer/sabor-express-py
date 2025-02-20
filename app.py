import os

restaurants = []

def display_logo():
    print('*************')
    print('⟆Ꭿᑲ𝖮ᖇ ᕮⲭᕈᖇ∈⟆⟆')
    print('*************')

def display_options_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def register_restaurant():
    os.system('clear')
    print('Cadastrar Restaurante\n')
    restaurant_name = input('Digite o nome do restaurante: ')
    restaurants.append(restaurant_name)
    print(f'Restaurante {restaurant_name} cadastrado com sucesso!\n')
    input('Digite qualquer tecla para voltar ao menu principal. ')
    main()

def list_restaurants():
    os.system('clear')
    print('Listar Restaurantes')

def activate_restaurant():
    os.system('clear')
    print('Ativar Restaurante')

def exit_program():
    os.system('clear')
    print('\nPrograma finalizado!')

def invalid_option():
    print('Opção inválida!')
    input('Digite qualquer tecla para voltar ao menu principal.')
    main()

def chosen_menu_option():
    try:
        chosen_option = int(input('\nEscolha uma opção: '))

        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            activate_restaurant()
        elif chosen_option == 4:
            exit_program()
        else:
            invalid_option()      
    except:
        invalid_option() 

def main():
    os.system('clear')
    display_logo()
    display_options_menu()
    chosen_menu_option()

if __name__ == '__main__':
    main()
