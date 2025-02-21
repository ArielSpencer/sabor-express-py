import os

restaurants = []

def display_logo():
    print('*************')
    print('⟆Ꭿᑲ𝖮ᖇ ᕮⲭᕈᖇ∈⟆⟆')
    print('*************\n')

def display_options_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair')

def display_subtitle(text):
    os.system('clear')
    print(f'{text}\n')

def back_to_menu():
    input('\nDigite "Enter" para voltar ao menu principal. ')
    main()

def register_restaurant():
    display_subtitle('Cadastrar Restaurante')

    restaurant_name = input('Digite o nome do restaurante: ')
    restaurants.append(restaurant_name)
    print(f'Restaurante {restaurant_name} cadastrado com sucesso!')

    back_to_menu()

def list_restaurants():
    display_subtitle('Listar Restaurantes')

    for restaurant in restaurants:
        print(f'- {restaurant}')
    
    back_to_menu()

def activate_restaurant():
    display_subtitle('Ativar Restaurante')

    back_to_menu()

def exit_program():
    display_subtitle('Programa finalizado!')

def invalid_option():
    print('Opção inválida!')
    back_to_menu()

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
